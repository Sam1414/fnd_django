from django import forms


class news_form(forms.Form):
    link = forms.CharField(label='link')
    # heading = forms.CharField(label='heading')
    # content = forms.CharField(label='content')
