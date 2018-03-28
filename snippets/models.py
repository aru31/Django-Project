from django.db import models

# Create your models here.


class Snippet(models.Model):
	title = models.CharField(max_length = 30)
	content = models.TextField()
	datetime_created = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	snippet = models.ForeignKey(to = 'Snippet', on_delete = models.CASCADE)
	content = models.TextField()
	datetime_created = models.DateTimeField(auto_now = True)

	def __str__(self):
		return "{0}: {1}".format(str(self.snippet), self.content)
