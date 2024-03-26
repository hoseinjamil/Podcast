from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField()
    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    body = forms.CharField(max_length=250, widget=forms.Textarea(attrs={"class": "form-control"}))