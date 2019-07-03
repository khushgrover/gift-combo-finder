from django.db import models

class Combo(models.Model):
	file = models.FileField(upload_to='giftcombo/')
	lowerbound = models.IntegerField()
	upperbound = models.IntegerField()

	def __str__(self):
		return self.file