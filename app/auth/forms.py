from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo
from ..models import User
from wtforms import ValidationError
from flask_login import current_user

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),Email(),Length(1,64)],render_kw = {"placeholder": "Электрондық пошта"})
    password = PasswordField("Құпия сөз", validators=[DataRequired()],render_kw = {"placeholder": "Құпия сөз"})
    remember_me = BooleanField("Мені есте сақта")
    submit = SubmitField("Кіру")

class RegisterationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),Email(), Length(1,64)])
    username = StringField("Пайдаланушы аты", validators=[DataRequired(), Length(1,64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                          'Пайдаланушы аттарында тек әріптер, сандар, нүктелер немесе астын сызу белгілері болуы керек')])
    password = PasswordField("Құпия сөз", validators=[DataRequired(),EqualTo("password2","Құпия сөздер бірдей болуы тиіс")])
    password2 = PasswordField("Құпия сөзді Растау", validators=[DataRequired(),EqualTo("құпия сөз","Құпия сөздер бірдей болуы тиіс")])
    submit = SubmitField("Тіркелу")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is not None:
            raise ValidationError("Электрондық пошта тіркелген")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first() is not None:
            raise ValidationError("Қолданыстағы пайдаланушы аты")


class changePasswordForm(FlaskForm):
    originalPassword = PasswordField("Бастапқы құпия сөз", validators=[DataRequired()])
    password = PasswordField("Жаңа Құпия Сөз", validators=[DataRequired(),EqualTo("password2","Құпия сөздер бірдей болуы тиіс")])
    password2 = PasswordField("Құпия сөзді Растау", validators=[DataRequired(),EqualTo("password","Құпия сөздер бірдей болуы тиіс")])
    submit = SubmitField("Құпия сөзді өзгерту")

    def validate_originalPassword(self, field):
        if not current_user.verify_password(field.data):
            raise ValidationError("Бастапқы құпия сөз дұрыс емес")

    def validate_password(self, field):
        if field.data == self.originalPassword.data:
            raise ValidationError("Жаңа құпия сөз түпнұсқа парольмен бірдей болмауы керек!")


class forgetPasswordRequestForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(1,64)])
    submit = SubmitField("Құпия сөзді ұмыттыңыз ба")

class resetPasswordForm(FlaskForm):
    password = PasswordField("Жаңа Құпия Сөз", validators=[DataRequired(),EqualTo("password2","Құпия сөздер бірдей болуы тиіс")])
    password2 = PasswordField("Құпия сөзді Растау", validators=[DataRequired(),EqualTo("password","Құпия сөздер бірдей болуы тиіс")])
    submit = SubmitField("Құпиясөзді қалпына келтіру")    



    