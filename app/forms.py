from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, \
    SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from flask_babel import _, lazy_gettext as _l
from app.models import User

class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField('Remembber Me')
    submit = SubmitField(_l('Sign in'))

class RegistrationForm(FlaskForm):
    username: str = StringField(_l('Username'), validators=[DataRequired()])
    email: str = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password: str = PasswordField(_l('Password'), validators=[DataRequired()])
    password2: str = PasswordField(_l('Repeat Password'), 
        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user: User = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different username'))
    
    def validate_email(self, email):
        user: User = User.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different email address'))

class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))

class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Request Password Reset'))

class EditProfileForm(FlaskForm):
    username: str = StringField(_l('Username'), validators=[DataRequired()])
    about_me: str = TextAreaField(_l('About me'), validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        #print("orig name:", original_username)

    def validate_username(self, username):
        print("username:", username.data, ", orig name:", self.original_username)
        if username.data != self.original_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))

class EmptyForm(FlaskForm):
    submit = SubmitField(_l('Submit'))

class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Submit'))