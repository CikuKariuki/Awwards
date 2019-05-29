from django import forms
from .models import Posts,Rates,Comments

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['profile']
        widgets = {
            'tag':forms.CheckboxSelectMultiple(),
        }
class VotesForm(forms.ModelForm):
    class Meta:
        model = Rates
        fields = ('design','usability','content')
        

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comments',)