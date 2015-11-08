from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User, AnonymousUser

# Create your models here.
def validate_date_in_past(value):
	if value >= date.today():
		raise ValidationError("Date Must Be in the Past, Please.")

class Profile(models.Model):
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User)
    birthday = models.DateField(null=True, blank=True, validators=[validate_date_in_past])
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    followed = models.ManyToManyField("Profile", related_name="followers")

    def __str__(self):
        return str(self.user)


def get_profile(user, save=False):
    if type(user) == AnonymousUser:
        return None
    else:
        try:
            profile = user.profile
        except Profile.DoesNotExist:
            profile = Profile()
            profile.user = user
            if save: profile.save()
        finally:
            return profile