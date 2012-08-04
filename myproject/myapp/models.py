from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
  user = models.ForeignKey(User, unique=True)
  biography = models.CharField(max_length=160)
  url = models.URLField()

  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      UserProfile.objects.create(user=instance)

  post_save.connect(create_user_profile, sender=User)

  def __unicode__(self):
    return self.user

class UserProfileForm(ModelForm):
  name = models.CharField(max_length=60)
  
  class Meta:
    model = UserProfile


