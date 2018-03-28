from django import forms

class SnippetForm(forms.Form):
	title = forms.CharField(label = 'Title', max_length=30)
	content = forms.CharField(label = 'Content', widget = forms.Textarea)
