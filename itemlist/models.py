from django.db import models


def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])


class Item(models.Model):
	itemname = models.CharField(max_length=200)
	discribe = models.TextField()
	price = models.IntegerField()
	image = models.ImageField(upload_to=content_file_name)
	weight = models.IntegerField()

	def __str__(self):
		return self.itemname

