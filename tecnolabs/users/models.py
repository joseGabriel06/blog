from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _



USER_TYPE_CHOICES = (
      (1, 'estandar'),
      (2, 'desarrollador'),
  )

class Role(models.Model):
  '''
  The Role entries are managed by the system,
  automatically created via a Django data migration.
  '''
  ESTANDAR = 1
  DESARROLLADOR = 2 
  
  
  
  
  ROLE_CHOICES = (
      (ESTANDAR, 'ESTANDAR'),
      (DESARROLLADOR, 'desarrollador'),
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_id_display()



@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,null=True,blank=False)

    
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
