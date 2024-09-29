from django import forms 
from .models import *

class ArticleFormOld(forms.Form):
  title = forms.CharField()
  content = forms.CharField()


  def clean_title(self):
    cleaned_data = self.cleaned_data
    title = cleaned_data.get('title')
    return title
  
class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = '__all__'