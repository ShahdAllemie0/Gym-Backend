from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Gym,Class,Booking

#""""""Auth"""""""""
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username']


class SignUpSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password', 'first_name', 'last_name']

	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		first_name = validated_data['first_name']
		last_name = validated_data['last_name']
		new_user = User(username=username, first_name=first_name, last_name=last_name)
		new_user.set_password(password)
		new_user.save()
		return validated_data



#""""""GYM"""""""""
class GymSerializer(serializers.ModelSerializer):
	class Meta:
		model = Gym
		fields = '__all__'


class CreateGymSerializer(serializers.ModelSerializer):
	class Meta:
		model = Gym
		fields='__all__'


class GymUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Gym
		fields='__all__'



#""""""Class"""""""""
class CreateClassSerializer(serializers.ModelSerializer):
  class Meta:
	  model=Class
	  fields='__all__'

class ClassSerializer(serializers.ModelSerializer):
	class Meta:
		model = Class
		fields = '__all__'



#""""""Booking"""""""""
class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model= Booking
		exclude = ['user']
