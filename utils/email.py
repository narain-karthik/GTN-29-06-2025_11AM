import smtplib
from email.mime.text import MIMEText
from flask import current_app
import logging


def get_email_settings():
    """Get email settings from Master Data or return defaults"""
    try:
        from models import EmailSettings
        settings = EmailSettings.query.filter_by(is_active=True).first()
        
        if settings:
            return {
                'smtp_server': settings.smtp_server,
                'smtp_port': settings.smtp_port,
                'smtp_username': settings.smtp_username,
                'smtp_password': settings.smtp_password,
                'use_tls': settings.use_tls,
                'from_email': settings.from_email or settings.smtp_username,
                'from_name': settings.from_name or 'GTN IT Helpdesk'
            }
        else:
            # Fallback to hardcoded values if no settings found
            logging.warning("No active email settings found in Master Data, using fallback values")
            return {
                'smtp_server': 'smtp.gmail.com',
                'smtp_port': 587,
                'smtp_username': 'narainjkans@gmail.com',
                'smtp_password': 'hefh vudq kkly wfsd',
                'use_tls': True,
                'from_email': 'narainjkans@gmail.com',
                'from_name': 'GTN IT Helpdesk'
            }
    except Exception as e:
        logging.error(f"Error getting email settings: {e}")
        # Fallback to hardcoded values on error
        return {
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'smtp_username': 'narainjkans@gmail.com',
            'smtp_password': 'hefh vudq kkly wfsd',
            'use_tls': True,
            'from_email': 'narainjkans@gmail.com',
            'from_name': 'GTN IT Helpdesk'
        }


def send_assignment_email(to_email, ticket_id, assignee_name):
    """Send ticket assignment email using Master Data email settings"""
    try:
        # Get email settings from Master Data
        email_settings = get_email_settings()
        
        # Email content
        subject = f"You have been assigned Ticket #{ticket_id}"
        body = f"Hello {assignee_name},\n\nYou have been assigned to Ticket #{ticket_id}. Please check the portal for details.\n\nBest regards,\n{email_settings['from_name']}"

        # Create message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = f"{email_settings['from_name']} <{email_settings['from_email']}>"
        msg['To'] = to_email

        # Send email
        with smtplib.SMTP(email_settings['smtp_server'], email_settings['smtp_port']) as server:
            if email_settings['use_tls']:
                server.starttls()
            server.login(email_settings['smtp_username'], email_settings['smtp_password'])
            server.sendmail(email_settings['from_email'], [to_email], msg.as_string())
            
        logging.info(f"Assignment email sent successfully to {to_email} for ticket #{ticket_id}")
        return True
        
    except Exception as e:
        logging.error(f"Failed to send assignment email: {e}")
        return False


def send_notification_email(to_email, subject, body, ticket_id=None):
    """Send general notification email using Master Data email settings"""
    try:
        # Get email settings from Master Data
        email_settings = get_email_settings()
        
        # Create message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = f"{email_settings['from_name']} <{email_settings['from_email']}>"
        msg['To'] = to_email

        # Send email
        with smtplib.SMTP(email_settings['smtp_server'], email_settings['smtp_port']) as server:
            if email_settings['use_tls']:
                server.starttls()
            server.login(email_settings['smtp_username'], email_settings['smtp_password'])
            server.sendmail(email_settings['from_email'], [to_email], msg.as_string())
            
        logging.info(f"Notification email sent successfully to {to_email}")
        return True
        
    except Exception as e:
        logging.error(f"Failed to send notification email: {e}")
        return False
