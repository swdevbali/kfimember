from django.db import models
from django.contrib.auth.models import User

class SertifikatModal(models.Model):
	user = models.ForeignKey(User)
	nomor = models.CharField(max_length=30)
	jumlah = models.FloatField(default = 0)