from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, SubmitField, EmailField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional
from models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class TicketForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=5, max=200)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10)])
    category = SelectField('Category', choices=[
        ('Hardware', 'Hardware'),
        ('Software', 'Software')
    ], validators=[DataRequired()])
    priority = SelectField('Priority', choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical')
    ], validators=[DataRequired()])
    system_name = StringField('System Name', render_kw={'placeholder': 'Enter your computer/system name'})
    image = FileField('Upload File (Optional)', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'pdf', 'doc', 'docx', 'xls', 'xlsx'], 'Images, PDF, Word, and Excel files only!')])
    submit = SubmitField('Create Ticket')

class UpdateTicketForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=5, max=200)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10)])
    category = SelectField('Category', choices=[
        ('Hardware', 'Hardware'),
        ('Software', 'Software')
    ], validators=[DataRequired()])
    priority = SelectField('Priority', choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical')
    ], validators=[DataRequired()])
    status = SelectField('Status', choices=[
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed')
    ], validators=[DataRequired()])
    submit = SubmitField('Update Ticket')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired(), Length(min=5)])
    submit = SubmitField('Add Comment')

class UserRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=80)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    department = StringField('Department', validators=[Length(max=100)])
    role = SelectField('Role', choices=[
        ('user', 'User'),
        ('super_admin', 'Super Admin')
    ], validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Register')

class UserProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=50)])
    role = SelectField('Role', choices=[('user', 'User'), ('super_admin', 'Super Admin')], validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    department = StringField('Department', validators=[Length(max=100)])
    system_name = StringField('System Name', validators=[Length(max=100)])
    password = PasswordField('Password', validators=[Optional(), Length(min=6, max=128)])
    submit = SubmitField('Update Profile')

class AssignTicketForm(FlaskForm):
    assigned_to = SelectField('Assign To', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Assign Ticket')
    
    def __init__(self, *args, **kwargs):
        super(AssignTicketForm, self).__init__(*args, **kwargs)
        self.assigned_to.choices = [(user.id, user.full_name) for user in User.query.filter_by(role='super_admin').all()]


# Master Data Forms
class MasterDataCategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[DataRequired(), Length(min=2, max=50)])
    description = TextAreaField('Description', validators=[Length(max=200)])
    is_active = BooleanField('Active', default=True)
    submit = SubmitField('Save Category')


class MasterDataPriorityForm(FlaskForm):
    name = StringField('Priority Name', validators=[DataRequired(), Length(min=2, max=20)])
    description = TextAreaField('Description', validators=[Length(max=200)])
    level = SelectField('Level', choices=[
        (1, '1 - Low'),
        (2, '2 - Medium'),
        (3, '3 - High'),
        (4, '4 - Critical')
    ], coerce=int, validators=[DataRequired()])
    color_code = StringField('Color Code', validators=[Length(max=7)], render_kw={'placeholder': '#007bff'})
    is_active = BooleanField('Active', default=True)
    submit = SubmitField('Save Priority')


class MasterDataStatusForm(FlaskForm):
    name = StringField('Status Name', validators=[DataRequired(), Length(min=2, max=20)])
    description = TextAreaField('Description', validators=[Length(max=200)])
    color_code = StringField('Color Code', validators=[Length(max=7)], render_kw={'placeholder': '#28a745'})
    is_active = BooleanField('Active', default=True)
    submit = SubmitField('Save Status')


class MasterDataDepartmentForm(FlaskForm):
    name = StringField('Department Name', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[Length(max=200)])
    manager_name = StringField('Manager Name', validators=[Length(max=100)])
    is_active = BooleanField('Active', default=True)
    submit = SubmitField('Save Department')


class SystemSettingsForm(FlaskForm):
    setting_key = StringField('Setting Key', validators=[DataRequired(), Length(min=2, max=100)])
    setting_value = TextAreaField('Setting Value')
    setting_type = SelectField('Type', choices=[
        ('text', 'Text'),
        ('number', 'Number'),
        ('boolean', 'Boolean'),
        ('json', 'JSON')
    ], validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(max=200)])
    is_active = BooleanField('Active', default=True)
    submit = SubmitField('Save Setting')
