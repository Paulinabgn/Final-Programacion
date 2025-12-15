from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, FileField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email, Length
from flask_wtf.file import FileAllowed ,FileField, FileSize

class FormRegistro(FlaskForm):
    nombre = StringField(label="Nombre", validators=[DataRequired()])
    apellido = StringField(label="Apellido", validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    username = StringField(label="Nombre de Usuario", validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=4), EqualTo('confirm', message='Las contraseñas deben coincidir')])
    confirm = PasswordField(label='Repetir Password', validators=[DataRequired()])
    claustro = SelectField(label='Claustro',choices=[('Docente','Docente'),('PAyS','PAyS'),('Estudiante','Estudiante')],validators=[DataRequired()])
    submit = SubmitField(label='Registrar')

class FormLogin(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField(label='Ingresar')

class ReclamoForm(FlaskForm):
    id = HiddenField(label='')   
#    asunto = StringField(label='Asunto', validators=[DataRequired()])
    contenido = StringField(label='Contenido', validators=[DataRequired()])
    imagen = FileField('Adjuntar imagen', validators = [
        FileAllowed(['jpg', 'jpeg', 'png'], 'Solo se permiten archivos de tipo jpg, jpeg, png'),
        FileSize(max_size = 5 * 1024 *1024, message = 'El archivo no debe superar los 5MB de tamano.')
    ])
    submit = SubmitField(label='Crear reclamo')