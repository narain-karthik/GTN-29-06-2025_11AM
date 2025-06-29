# Master Data Management Guide

## Overview

The Master Data Management system provides Super Admins with centralized control over all reference data and system configurations in the GTN Engineering IT Helpdesk. This comprehensive guide covers how to manage all core data elements that drive the helpdesk operations.

## Accessing Master Data

1. **Login as Super Admin** - Only Super Admin accounts have access to Master Data
2. **Navigate to Master Data** - Click "Master Data" in the top navigation menu
3. **Dashboard Overview** - View summary statistics and quick access to all management areas

## Master Data Components

### 1. Categories Management 📁

**Purpose**: Define ticket categories to classify support requests

**Default Categories**:
- Hardware (computer issues, equipment problems)
- Software (application issues, system software)

**How to Manage**:
1. Click "Manage" button in Categories section
2. Use the left form to add new categories
3. Fill required fields:
   - **Category Name**: Short, descriptive name
   - **Description**: Detailed explanation of category scope
   - **Active Status**: Enable/disable category
4. View existing categories in the table
5. Edit categories using the edit button

**Best Practices**:
- Keep category names clear and concise
- Ensure categories don't overlap in scope
- Deactivate instead of deleting categories with existing tickets

---

### 2. Priority Levels Management 🚩

**Purpose**: Set ticket priority levels with visual indicators

**Standard Priority Levels**:
1. **Low** (Level 1) - Non-urgent issues
2. **Medium** (Level 2) - Standard business issues  
3. **High** (Level 3) - Important business impact
4. **Critical** (Level 4) - System down, urgent

**How to Manage**:
1. Click "Manage" button in Priority Levels section
2. Create new priorities with:
   - **Priority Name**: Clear identifier
   - **Level**: Numeric ranking (1-4)
   - **Color Code**: Hex color for visual distinction
   - **Description**: When to use this priority
   - **Active Status**: Enable/disable priority
3. Use color picker for consistent visual branding

**Color Recommendations**:
- **Low**: Green (#28a745)
- **Medium**: Blue (#007bff)  
- **High**: Orange (#fd7e14)
- **Critical**: Red (#dc3545)

---

### 3. Status Types Management 📊

**Purpose**: Track ticket progression through workflow stages

**Standard Status Types**:
- **Open** - New tickets awaiting review
- **In Progress** - Tickets being actively worked
- **Resolved** - Issues fixed, awaiting confirmation
- **Closed** - Completed tickets

**How to Manage**:
1. Click "Manage" button in Ticket Statuses section
2. Define status types with:
   - **Status Name**: Clear workflow stage name
   - **Color Code**: Visual indicator color
   - **Description**: What this status means
   - **Active Status**: Enable/disable status
3. Maintain logical workflow progression

**Color Recommendations**:
- **Open**: Blue (#007bff)
- **In Progress**: Yellow (#ffc107)
- **Resolved**: Green (#28a745)
- **Closed**: Gray (#6c757d)

---

### 4. Departments Management 🏢

**Purpose**: Organize users by organizational structure

**How to Manage**:
1. Click "Manage" button in Departments section
2. Add departments with:
   - **Department Name**: Official department name
   - **Manager Name**: Department head/manager
   - **Description**: Department responsibilities
   - **Active Status**: Enable/disable department
3. Assign users to departments for better organization

**Examples**:
- IT Support (Manager: John Smith)
- Human Resources (Manager: Jane Doe)
- Finance (Manager: Mike Johnson)
- Operations (Manager: Sarah Wilson)

---

### 5. System Users Management 👥

**Purpose**: Manage all system users and their access levels

**User Roles**:
- **User**: Can create tickets, view own tickets, update profile
- **Super Admin**: Full system access, can manage all data and users

**How to Manage**:
1. Click "Manage" button in System Users section (redirects to User Management)
2. View user overview in Master Data dashboard
3. Monitor user statistics and recent additions

**User Management Functions**:
- Create new user accounts
- Edit user profiles and roles
- Assign users to departments
- Deactivate user accounts
- View user activity and tickets

---

### 6. System Settings Management ⚙️

**Purpose**: Configure system-wide parameters and behaviors

**Setting Types**:
- **Text**: Simple text values
- **Number**: Numeric configurations
- **Boolean**: True/false settings
- **JSON**: Complex configuration objects

**How to Manage**:
1. Click "Manage Settings" button in System Settings section
2. Add new settings with:
   - **Setting Key**: Unique identifier (use underscore_format)
   - **Setting Type**: Data type for validation
   - **Setting Value**: The actual configuration value
   - **Description**: What this setting controls
   - **Active Status**: Enable/disable setting

**Common Settings Examples**:
```
max_file_size (Number): 10485760
email_notifications (Boolean): true
session_timeout (Number): 3600
maintenance_mode (Boolean): false
allowed_file_types (JSON): ["jpg","png","pdf","doc","docx"]
support_email (Text): support@gtnengineering.com
```

---

## Master Data Workflow

### Initial Setup Process

1. **Configure Departments** - Set up organizational structure
2. **Define Categories** - Establish ticket classification system
3. **Set Priority Levels** - Create urgency framework with colors
4. **Configure Status Types** - Define workflow stages with colors
5. **Create User Accounts** - Add team members with appropriate roles
6. **Configure System Settings** - Set operational parameters

### Ongoing Management

1. **Regular Review** - Monthly review of all master data for relevance
2. **User Feedback** - Collect input from team on category/priority effectiveness
3. **Analytics Review** - Use reports to identify unused or problematic data
4. **Documentation Updates** - Keep descriptions current and helpful
5. **Access Control** - Regular audit of user roles and permissions

---

## Best Practices

### Data Consistency
- Use consistent naming conventions across all master data
- Maintain clear descriptions for all entries
- Implement logical color schemes that are accessible
- Regular cleanup of inactive/unused data

### User Experience
- Keep categories and statuses intuitive for end users
- Use meaningful priority levels that reflect business needs
- Ensure department structure matches organizational reality
- Provide clear guidance in descriptions

### System Performance
- Avoid creating excessive categories or statuses
- Deactivate rather than delete referenced data
- Monitor system settings impact on performance
- Regular backup of master data configurations

### Security
- Limit Master Data access to trusted Super Admins
- Document all changes with reasons
- Regular review of user roles and permissions
- Audit trail for sensitive configuration changes

---

## Troubleshooting

### Common Issues

**Categories Not Appearing in Ticket Forms**
- Check if category is marked as Active
- Verify category name doesn't contain special characters
- Restart application if needed

**Priority Colors Not Displaying**
- Ensure valid hex color codes are used
- Check browser cache and refresh
- Verify color accessibility standards

**Users Cannot Access Features**
- Confirm user role assignments
- Check department associations
- Verify account active status

**System Settings Not Taking Effect**
- Confirm setting is marked as Active
- Check setting value format matches type
- Application restart may be required for some settings

### Getting Support

For technical issues with Master Data management:
1. Check system logs for error messages
2. Verify database connectivity
3. Contact system administrator
4. Document issue details for support

---

## Quick Reference

### Navigation Path
**Home → Login (Super Admin) → Master Data → Select Component**

### Key Actions
- **Add**: Use forms on management pages
- **Edit**: Click edit buttons in data tables  
- **Activate/Deactivate**: Toggle status in forms
- **View**: Browse data tables and overview cards

### Color Picker Usage
- Click color field to open picker
- Enter hex codes directly (#ffffff)
- Use color names for common colors
- Test accessibility with contrast checkers

---

*Last Updated: June 29, 2025*  
*GTN Engineering (India) Ltd - IT Team*