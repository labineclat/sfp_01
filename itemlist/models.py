from django.db import models
from django.utils import timezone

class Item(models.Model):
	itemname = models.CharField(max_length=200)
	discribe = models.TextField()
	price = models.IntegerField()
	image = models.ImageField()
	weight = models.IntegerField()

	def __str__(self):
		return self.itemname

