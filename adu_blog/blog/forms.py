from django import forms


class BlogEntry(forms.Form):
    name = forms.CharField(label='Your name', max_length=50)
    title = forms.CharField(label='Your name', max_length=50)
