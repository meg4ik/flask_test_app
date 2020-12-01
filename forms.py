from wtforms_alchemy import ModelForm
from models import person, articles

class PersonForm(ModelForm):
    class Meta:
        model = person 

class ArticlesForm(ModelForm):
    class Meta:
        model = articles