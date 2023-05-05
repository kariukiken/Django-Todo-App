from django.db import models

# Create your models here.


class tasks(models.Model):
	name = models.CharField(max_length=50, unique=True)
	In_progress = models.BooleanField(default=True)
	dead_line = models.DateField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name