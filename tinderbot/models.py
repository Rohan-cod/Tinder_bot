from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


class Account(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
