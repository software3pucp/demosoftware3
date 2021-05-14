from django.db import models
from django.contrib.auth.models import AbstractUser
import unicodedata


# Create your models here.
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


# Create your models here.
def substring_after(s, delim):
    return s.rpartition(delim)[-1]


def upload_location(instance, filename):
    extension = substring_after(filename, '.')
    return 'img/%s.%s' % (remove_accents(instance.first_name), extension)


class User(AbstractUser):
    code = models.CharField(max_length=8, default='11111111')
    photo = models.ImageField(null=True, blank=True, upload_to=upload_location)
