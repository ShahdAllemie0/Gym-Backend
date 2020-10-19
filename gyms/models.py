from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
#""""""GYM"""""""""
class Gym(models.Model):
    name=models.CharField(max_length=120)
    image = models.ImageField(blank = True,null=True)

    def __str__(self):
        return self.name


#""""""Class"""""""""
class Class(models.Model):
    CLASS_TYPES = (
        ('Aerial', 'Aerial',),
        ('Barre', 'Barre',),
        ('Bootcamp', 'Bootcamp',),
        ('Boxing', 'Boxing',),
        ('Circuit training', 'Circuit training',),
        ('Crossfit', 'Crossfit',),
        ('Cycling', 'Cycling',),

    )
    title=models.CharField(max_length=120)
    type=models.CharField( max_length=40,choices=CLASS_TYPES)
    date=models.DateField()
    time=models.TimeField()
    isFree=models.BooleanField()
    gym=models.ForeignKey(Gym,on_delete=models.CASCADE,related_name='classGym')


    def __str__(self):
        return self.title

# class GymUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(blank = True,null=True)
#

#""""""Booking"""""""""
class Booking(models.Model):
    Booking_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    classes=models.ForeignKey(Class,on_delete=models.CASCADE,related_name='classes')

    def __str__(self):
        return f'{self.user} - {self.Booking_id}'

#""""""Profile"""""""""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
