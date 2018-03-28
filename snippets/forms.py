from django import forms
from snippets.models import Comment

class SnippetForm(forms.Form):
	title = forms.CharField(label = 'Title', max_length=30)
	content = forms.CharField(label = 'Content', widget = forms.Textarea)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content']
