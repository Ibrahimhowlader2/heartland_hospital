from django.db import models
from django.contrib.auth.models import User

# Image Upload Function
def upload_status_image(instance,filename):
    return "patient/images/{user}/{filename}".format(user = instance.user,filename = filename)
# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='patient/images/')
    # image = models.ImageField(upload_to=upload_status_image,null=True)
    mobile_no = models.CharField(max_length = 12)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
