from wtforms import Form, StringField
from wtforms.validators import  DataRequired

class TodosForm(Form):

    item = StringField("New Todo", validators=[DataRequired()])
    category = StringField("New Category", validators=[DataRequired()])
