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


def log_email_notification(to_email, subject, message_type, status, error_message=None, ticket_id=None, user_id=None):
    """Log email notification to database"""
    try:
        from flask import current_app
        with current_app.app_context():
            from models import EmailNotificationLog
            from app import db
            
            log_entry = EmailNotificationLog(
                to_email=to_email,
                subject=subject,
                message_type=message_type,
                status=status,
                error_message=error_message,
                ticket_id=ticket_id,
                user_id=user_id
            )
            db.session.add(log_entry)
            db.session.commit()
            logging.info(f"Email notification logged: {status} to {to_email}")
    except Exception as e:
        logging.error(f"Failed to log email notification: {e}")

def send_assignment_email(to_email, ticket_id, assignee_name):
    """Send ticket assignment email using Master Data email settings"""
    subject = f"You have been assigned Ticket #{ticket_id}"
    
    try:
        # Get email settings from Master Data
        email_settings = get_email_settings()
        
        logging.info(f"Attempting to send assignment email to {to_email} for ticket #{ticket_id}")
        logging.info(f"Using SMTP server: {email_settings['smtp_server']}:{email_settings['smtp_port']}")
        
        # Email content
        body = f"Hello {assignee_name},\n\nYou have been assigned to Ticket #{ticket_id}. Please check the portal for details.\n\nBest regards,\n{email_settings['from_name']}"

        # Create message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = f"{email_settings['from_name']} <{email_settings['from_email']}>"
        msg['To'] = to_email

        # Send email with detailed logging
        with smtplib.SMTP(email_settings['smtp_server'], email_settings['smtp_port']) as server:
            logging.info("SMTP connection established")
            
            if email_settings['use_tls']:
                server.starttls()
                logging.info("TLS enabled")
                
            server.login(email_settings['smtp_username'], email_settings['smtp_password'])
            logging.info("SMTP authentication successful")
            
            server.sendmail(email_settings['from_email'], [to_email], msg.as_string())
            logging.info("Email sent successfully")
            
        # Log successful email (handle test case and extract numeric ID from ticket numbers)
        if ticket_id == "TEST":
            log_ticket_id = None
        elif isinstance(ticket_id, str) and ticket_id.startswith("GTN-"):
            # Extract numeric part from GTN-000001 format
            try:
                log_ticket_id = int(ticket_id.split("-")[1])
            except (IndexError, ValueError):
                log_ticket_id = None
        else:
            log_ticket_id = ticket_id
        log_email_notification(to_email, subject, 'ticket_assigned', 'sent', ticket_id=log_ticket_id)
        logging.info(f"Assignment email sent successfully to {to_email} for ticket #{ticket_id}")
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        error_msg = f"SMTP Authentication failed: {e}. Check Gmail app password or enable 2-factor authentication"
        logging.error(error_msg)
        # Handle ticket ID conversion for error logging
        if ticket_id == "TEST":
            log_ticket_id = None
        elif isinstance(ticket_id, str) and ticket_id.startswith("GTN-"):
            try:
                log_ticket_id = int(ticket_id.split("-")[1])
            except (IndexError, ValueError):
                log_ticket_id = None
        else:
            log_ticket_id = ticket_id
        log_email_notification(to_email, subject, 'ticket_assigned', 'failed', error_msg, log_ticket_id)
        return False
    except smtplib.SMTPRecipientsRefused as e:
        error_msg = f"Recipient email rejected: {e}"
        logging.error(error_msg)
        # Handle ticket ID conversion for error logging
        if ticket_id == "TEST":
            log_ticket_id = None
        elif isinstance(ticket_id, str) and ticket_id.startswith("GTN-"):
            try:
                log_ticket_id = int(ticket_id.split("-")[1])
            except (IndexError, ValueError):
                log_ticket_id = None
        else:
            log_ticket_id = ticket_id
        log_email_notification(to_email, subject, 'ticket_assigned', 'failed', error_msg, log_ticket_id)
        return False
    except smtplib.SMTPServerDisconnected as e:
        error_msg = f"SMTP server disconnected: {e}"
        logging.error(error_msg)
        # Handle ticket ID conversion for error logging
        if ticket_id == "TEST":
            log_ticket_id = None
        elif isinstance(ticket_id, str) and ticket_id.startswith("GTN-"):
            try:
                log_ticket_id = int(ticket_id.split("-")[1])
            except (IndexError, ValueError):
                log_ticket_id = None
        else:
            log_ticket_id = ticket_id
        log_email_notification(to_email, subject, 'ticket_assigned', 'failed', error_msg, log_ticket_id)
        return False
    except Exception as e:
        error_msg = f"Failed to send assignment email: {e} (Type: {type(e).__name__})"
        logging.error(error_msg)
        # Handle ticket ID conversion for error logging
        if ticket_id == "TEST":
            log_ticket_id = None
        elif isinstance(ticket_id, str) and ticket_id.startswith("GTN-"):
            try:
                log_ticket_id = int(ticket_id.split("-")[1])
            except (IndexError, ValueError):
                log_ticket_id = None
        else:
            log_ticket_id = ticket_id
        log_email_notification(to_email, subject, 'ticket_assigned', 'failed', error_msg, log_ticket_id)
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
