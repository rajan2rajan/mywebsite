from .models import About,Videos
from django import forms



class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'



class ContactForm(forms.Form):
    Name        = forms.CharField(max_length=20)
    Email       = forms.EmailField(max_length=100)
    Subject     = forms.CharField(max_length=30)
    Message     = forms.CharField(max_length=1000)



class VideoForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = '__all__'
