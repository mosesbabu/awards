from django import forms
from .models import Project,Profile,Rating

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['username','post_date','design','usability','creativity','content','overall_score','avatar','country']
        widgets={
        'colors':forms.CheckboxSelectMultiple(),
        'technologies':forms.CheckboxSelectMultiple(),
        'categories':forms.CheckboxSelectMultiple(),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=['overall_score','profile','project']
