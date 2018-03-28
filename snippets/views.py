from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from snippets.forms import SnippetForm
from snippets.models import Snippet

def create(request):
	if request.method == "GET":
		form = SnippetForm()
	elif request.method == "POST":
		form = SnippetForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			snippet = Snippet(title = data.get('title'), content = data.get('content'))
			snippet.save()
			return redirect('view', snippet.id)
	return render(request, 'snippets/create.html', {'form': form})

def view(request, key):
	if request.method == "GET":
		if Snippet.objects.filter(id = key).exists():
			snippet = Snippet.objects.get(id = key)
		else:
			raise Http404("Snippet Doesnot Exist")
	return render(request, 'snippets/view.html', {'key': key, 'title': snippet.title, 'content': snippet.content} )


