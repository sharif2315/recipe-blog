from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, DecimalField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Optional
from app.models import RecipeDifficulty


class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    duration = DecimalField('Duration', places=1, validators=[DataRequired()])
    difficulty = SelectField(
        'Difficulty',
        choices=[(d.value, d.name.title()) for d in RecipeDifficulty],
        coerce=lambda x: RecipeDifficulty(x) if isinstance(x, str) else x,
        validators=[Optional()],
    )
    servings_text = StringField('Serves', validators=[DataRequired()])
    # author
    image_filename = FileField(
        'Recipe Image', 
        validators=[FileAllowed(['jpg', 'jpeg', 'png', 'webp'], 'Images only!')]
    )
    submit = SubmitField('Save Recipe')