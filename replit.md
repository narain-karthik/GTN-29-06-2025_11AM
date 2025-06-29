# GTN Engineering IT Helpdesk System

## Overview

The GTN Engineering IT Helpdesk System is a comprehensive Flask-based web application designed to manage IT support tickets within an organization. The system features role-based access control with three distinct user levels (Super Admin, Admin, and User), automatic system information capture, and a complete ticket lifecycle management system.

## System Architecture

### Backend Architecture
- **Framework**: Flask with SQLAlchemy ORM
- **Database**: Multi-database support with automatic detection
  - PostgreSQL: Primary production database (default)
  - SQL Server: Enterprise production database with pyodbc connector
  - MySQL: Alternative production database with PyMySQL connector
- **Authentication**: Session-based authentication with role-based access control
- **Server**: Gunicorn WSGI server for production deployment

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Flask
- **CSS Framework**: Bootstrap 5.3.0 for responsive design
- **Icons**: Remix Icons for consistent iconography
- **JavaScript**: Vanilla JavaScript for client-side interactions

### Application Structure
```
├── main.py              # Application entry point
├── app.py               # Flask app configuration and initialization
├── routes.py            # URL routing and view functions
├── models.py            # Database models (User, Ticket, TicketComment)
├── forms.py             # WTForms form definitions
├── templates/           # Jinja2 HTML templates
└── static/             # CSS, JavaScript, and static assets
```

## Key Components

### Database Models
1. **User Model**: Handles user authentication, profile information, and role management
2. **Ticket Model**: Manages support tickets with full lifecycle tracking
3. **TicketComment Model**: Enables comment system for ticket updates

### Role-Based Access Control
- **Super Admin**: Full system access, user management, ticket oversight
- **Admin**: Ticket management, assignment capabilities
- **User**: Ticket creation and personal ticket management

### Automatic System Detection
- IP address capture for user tracking
- System name detection for better support context
- Integration with ticket creation process

### Forms and Validation
- WTForms integration for secure form handling
- Comprehensive validation for all user inputs
- CSRF protection enabled

## Data Flow

1. **User Authentication**: Session-based login with role verification
2. **Ticket Creation**: Users submit tickets with automatic system info capture
3. **Ticket Assignment**: Admins can assign tickets based on category specialization
4. **Ticket Management**: Status updates, comments, and resolution tracking
5. **Reporting**: Excel export functionality for administrative oversight

## External Dependencies

### Python Packages
- Flask (web framework)
- Flask-SQLAlchemy (database ORM)
- Flask-WTF (form handling)
- Flask-Login (authentication)
- Werkzeug (WSGI utilities)
- Gunicorn (production server)
- email-validator (email validation)
- openpyxl (Excel export functionality)

### Frontend Dependencies
- Bootstrap 5.3.0 (CSS framework)
- Remix Icons (icon library)

### Development Dependencies
- SQLite (development database)
- PostgreSQL packages (production ready)

## Deployment Strategy

### Development Environment
- SQLite database for local development
- Flask development server with debug mode
- Hot reload enabled for rapid development

### Production Environment
- Gunicorn WSGI server with autoscale deployment
- PostgreSQL database support configured
- ProxyFix middleware for proper header handling
- Environment-based configuration management

### Container Configuration
- Replit configuration with multiple modules (web, python-3.11, nodejs-20)
- Nixpkgs for system dependencies (openssl, postgresql)
- Port configuration for external access

## Changelog

- June 29, 2025: Implemented lite UI/UX design improvements:
  - Updated user profile page with clean white background and black text instead of gradient background
  - Created compact, medium-sized profile layout with optimized spacing and smaller elements
  - Made profile header more compact with smaller avatar, reduced padding, and condensed text sizes
  - Optimized form sections with reduced margins, smaller fonts, and better vertical spacing
  - Removed Quick Actions section from user profile to create cleaner, more focused layout
  - Replaced Security Settings section with informational card directing users to contact IT Team for password changes
  - Fixed search bar overflow in "My Support Tickets" section by implementing proper flexbox layout and responsive design
  - Reduced banner header size with smaller padding, font sizes, and margins for more compact appearance
  - Added proper CSS for section headers to prevent content overflow on mobile devices
- June 29, 2025: Updated all README files to reflect current system architecture:
  - Removed all Admin role references from README.md, README_Database_Schema.md, and README_Master_Data.md
  - Updated database schema documentation to include ticket_number field and specialization field
  - Added complete Master Data tables documentation (categories, priorities, statuses, email settings, etc.)
  - Updated project structure in README.md to reflect current file organization
  - Cleaned up unwanted file references and corrected role descriptions throughout documentation
- June 29, 2025: Applied lite design to "My Support Tickets" section in user dashboard:
  - Created clean, minimalist ticket cards with circular status icons matching reference image
  - Implemented horizontal card layout with color-coded status indicators (red, orange, green, gray)
  - Condensed ticket information with small tags and meta data for streamlined appearance
  - Reduced visual clutter with lighter borders, subtle shadows, and essential information only
- June 29, 2025: Simplified homepage layout for compact viewing without scrolling:
  - Removed extensive sections (features, user roles, call-to-action) from index.html
  - Created compact single-section design with header, professional content, and footer
  - Changed layout to centered single column with 60vh height for no-scroll experience
  - Maintained professional branding with "Professional IT Helpdesk Solutions" tagline
  - Kept essential "Access Helpdesk" button for user login functionality
- June 29, 2025: Completed user interface fixes and access control improvements:
  - Fixed 500 error in reports dashboard by restructuring SQLAlchemy query to return dictionary format
  - Removed specialization field from user profile template as requested
  - Enhanced logo visibility with improved CSS (increased container size, added overflow handling, better image scaling)
  - Implemented read-only user profiles for regular users - only Super Admins can edit profile information
  - Added permission checks and disabled form fields with appropriate user feedback messages
  - All user-reported issues successfully resolved
- June 29, 2025: Removed Super Admin deletion restriction - Super Admins can now delete other Super Admin accounts (only self-deletion is still prevented for safety)
- June 29, 2025: Added specialization field to User model allowing selection between Hardware and Software support expertise
- June 29, 2025: Fixed email notification tracking to properly handle ticket ID extraction from GTN-000001 format for database logging
- June 29, 2025: Successfully completed migration from Replit Agent to standard Replit environment with enhanced functionality and fixed email settings template:
  - Resolved 500 error in email settings page by fixing CSRF token handling in templates/master_data/email_settings.html
  - Changed test email functionality from POST form to GET link to avoid CSRF complications
  - Updated test_email_settings route to handle both GET and POST methods
- June 29, 2025: Successfully completed migration from Replit Agent to standard Replit environment with enhanced functionality:
  - Fixed PostgreSQL database connection and automatic provisioning
  - Created uploads directory to resolve 500 errors during ticket creation
  - Configured secure session management with SESSION_SECRET environment variable
  - Implemented automatic default master data creation on startup (Categories: 2, Priorities: 4, Statuses: 4)
  - Added Email Notification tracking dashboard with sent/failed statistics
  - Enhanced user profile UI with modern design matching provided reference
  - Fixed email notifications route 500 error with correct URL references
  - Verified all database tables are properly created and functional
  - Application running successfully on port 5000 with Gunicorn WSGI server
- June 29, 2025: Completed Master Data integration with full CRUD functionality and dynamic email configuration:
  - Fixed Master Data forms to dynamically load categories, priorities, and statuses from database instead of hardcoded values
  - Enhanced utils/email.py to read SMTP settings from Master Data database with fallback protection
  - Added complete delete functionality for all Master Data components with confirmation dialogs
  - Created edit_priority.html and edit_status.html templates with professional UI and color picker support
  - Updated priorities.html, statuses.html, and categories.html to include Edit, Activate/Deactivate, and Delete action buttons
  - Added delete routes in routes.py for categories, priorities, and statuses with proper error handling
  - Updated Master Data dashboard to show individual overview cards for Email Settings, Timezone Settings, and Backup Settings
  - Added JavaScript confirmDelete function with CSRF protection for secure deletion operations
  - Master Data system now provides complete control over application behavior with real-time updates
- June 29, 2025: Removed Department functionality from Master Data management system:
  - Deleted MasterDataDepartment model and database table
  - Removed MasterDataDepartmentForm from forms.py
  - Deleted manage_departments route and templates/master_data/departments.html
  - Updated Master Data dashboard to remove Department section and overview card
  - System now only manages Categories, Priorities, Statuses, and System Settings
- June 29, 2025: Successfully completed migration from Replit Agent to standard Replit environment:
  - Set up PostgreSQL database with automatic provisioning
  - Configured secure session management with SESSION_SECRET environment variable
  - Fixed Master Data Management system with missing template files
  - Created timezone_settings.html and backup_settings.html templates
  - Verified all database models and routes are working properly
  - Application running successfully on port 5000 with Gunicorn WSGI server
- June 29, 2025: Added comprehensive Master Data Management system for Super Admins:
  - Created centralized Master Data dashboard for controlling all system configuration
  - Added management interfaces for Categories, Priorities, Statuses, Departments, and System Settings
  - Integrated User Management into Master Data dashboard with user overview section
  - Implemented full CRUD operations with proper validation and forms
  - Added Master Data navigation link in Super Admin menu
  - Created database models for master data with proper relationships and timestamps
  - Designed professional UI with overview cards, data tables, and management forms
  - Color picker support for priorities and statuses with visual indicators
- June 29, 2025: Enhanced UI/UX for five key pages with modern design, interactive elements, and improved user experience:
  - Create Ticket: Progress indicators, drag-drop file upload, character counters, form validation
  - User Profile: Professional layout with avatar, stats sidebar, password strength indicators
  - Create User: Role permissions overview, password requirements, real-time validation
  - Manage Users: Advanced table with search, sorting, filtering, user stats overview
  - Reports Dashboard: Interactive charts, metrics cards, activity timeline, export functionality
- June 29, 2025: Successfully completed migration from Replit Agent to standard Replit environment with PostgreSQL database, secure session management, and full functionality
- June 28, 2025: Completed comprehensive documentation update with database schema, PostgreSQL setup guide, and updated README files
- June 28, 2025: Created modern UI/UX login page with split-screen design, floating labels, animated backgrounds, and role indicators
- June 28, 2025: Added comprehensive .gitignore file covering Python, Flask, database files, IDE files, and security-sensitive content
- June 28, 2025: Enhanced database schema documentation with PostgreSQL optimization, performance tuning, and monitoring guidelines
- June 28, 2025: Updated README files to reflect modern UI/UX features, simplified role structure, and Replit deployment instructions
- June 28, 2025: Cleaned up project by removing unwanted files (uploads, cache files) and documented file structure
- June 28, 2025: Implemented modern UI/UX design for home page with hero section, features showcase, user roles explanation, and smooth animations
- June 28, 2025: Added responsive design with gradient backgrounds, floating card animations, and smooth scrolling functionality
- June 28, 2025: Enhanced home page with professional branding, clear value proposition, and improved user experience
- June 28, 2025: Fixed datetime formatting issues in Excel export and template filters to handle None values properly
- June 28, 2025: Corrected template syntax errors in assign_work.html and updated assignment logic for simplified role structure
- June 28, 2025: Fixed URL routing errors caused by duplicate "super_" prefixes in template navigation links
- June 28, 2025: Successfully completed Admin role removal from the entire system - now only supports User and Super Admin roles for simplified management
- June 28, 2025: Updated all forms, routes, models, and templates to remove Admin role references and cleaned up access control logic
- June 28, 2025: Removed admin_dashboard.html template and admin_dashboard route as they're no longer needed
- June 28, 2025: Updated role-based access control to use super_admin_required decorator instead of admin_required
- June 28, 2025: Successfully completed migration from Replit Agent to Replit environment with PostgreSQL database and secure session management
- June 28, 2025: Simplified default user creation to only include Super Admin and test user (removed all default admin accounts)
- June 28, 2025: Enhanced Super Admin privileges to allow full control over all user accounts including other Super Admin accounts
- June 28, 2025: Removed frontend restrictions that previously prevented Super Admins from editing/deleting other Super Admin accounts
- June 28, 2025: Fixed user role editing bug where 'super_admin' role wasn't properly saved due to form choice mismatch
- June 28, 2025: Enhanced SMTP email notification system with proper environment variable configuration and error handling
- June 27, 2025: Successfully completed migration from Replit Agent to Replit environment with automatic PostgreSQL provisioning
- June 27, 2025: Enhanced ticket history display with new streamlined format showing Created By, Assigned By, Assigned To, and Status with colored badges
- June 27, 2025: Fixed edit ticket page template errors and property access issues for improved stability
- June 27, 2025: Updated all README documentation to reflect Replit integration and recent feature enhancements
- June 27, 2025: Added "Assigned By" tracking to monitor who assigns tickets to admins
- June 27, 2025: Super admins can now add comments directly when editing ticket status
- June 27, 2025: Enhanced Excel export to include "Assigned By" column for better tracking
- June 27, 2025: Added assignment history display in ticket details view
- June 27, 2025: Restricted ticket editing permissions for all users (admins and super admins)
- June 27, 2025: Admins can now only update ticket status - title, category, priority, and description are read-only after creation
- June 27, 2025: Enhanced attachment display with file type icons (PDF, Word, Excel, images) and clean filename presentation
- June 27, 2025: Added attachment indicators in all dashboard views to show which tickets have files
- June 27, 2025: Enhanced file upload system to support PDF, Word (.doc, .docx), and Excel (.xls, .xlsx) files in addition to images
- June 27, 2025: Fixed ticket creation errors and improved multiple file attachment handling
- June 27, 2025: Updated all README documentation to reflect new file attachment capabilities
- June 26, 2025: Successfully migrated from Replit Agent to Replit environment with PostgreSQL database
- June 26, 2025: Enhanced Super Admin user management with complete CRUD functionality:
  - Added "View User Details" feature showing user info, created tickets, and assigned tickets
  - Added "Edit User" functionality for updating user profile information
  - Added "Delete User" feature with data integrity protection and safety checks
- June 23, 2025: Cleaned up project by removing unwanted files (__pycache__, attached_assets) and added .gitignore
- June 23, 2025: Removed Network and Other categories from all pages (admin dashboard, super admin dashboard, reports dashboard)
- June 23, 2025: Fixed ticket creation 500 errors by creating uploads directory and improving file handling
- June 23, 2025: Fixed dashboard 500 errors by adding image_filename column to database
- June 23, 2025: Successfully migrated from Replit Agent to Replit environment with enhanced image upload functionality
- June 23, 2025: Added secure image upload system for tickets with admin-only viewing capabilities
- June 23, 2025: Updated ticket categories to Hardware and Software only (removed Network and Other)
- June 23, 2025: Enhanced database schema with image_filename field for ticket attachments
- June 23, 2025: Updated documentation in README.md and README_PostgreSQL_Setup.md
- June 22, 2025: Completed migration to Replit environment with PostgreSQL as primary database
- June 22, 2025: Enhanced system name detection to capture accurate client information per ticket
- June 22, 2025: Implemented modern UI/UX design with CSS custom properties and professional styling
- June 22, 2025: Created comprehensive PostgreSQL setup guide for Windows systems
- June 22, 2025: Added Microsoft SQL Server integration with comprehensive setup guide and connection testing
- June 22, 2025: Updated comprehensive README.md with complete setup instructions, user guides, and troubleshooting
- June 22, 2025: Added Reports Dashboard with visual analytics, assignment editing functionality, and MySQL support
- June 21, 2025: Initial setup

## User Preferences

Preferred communication style: Simple, everyday language.