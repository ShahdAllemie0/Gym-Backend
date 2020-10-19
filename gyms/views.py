from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from .models import Gym,Class,Booking
from .serializers import (SignUpSerializer,GymSerializer,CreateGymSerializer,GymUpdateSerializer,CreateClassSerializer,ClassSerializer,
BookingSerializer,GymDetailSerializer,)
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.filters import SearchFilter,OrderingFilter
from datetime import datetime
from django.core.mail import send_mail
from .permissions import IsBookingOwner, IsChangable
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

#""""""Token"""""""""
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
	def validate(self, attrs):
		data = super().validate(attrs)
		refresh = self.get_token(self.user)
		data['refresh'] = str(refresh)
		data['access'] = str(refresh.access_token)
		data['username'] = self.user.username
		data['email'] = self.user.email
		data['isAdmin']=self.user.IsAdminUser
		return data


class MyTokenObtainPairView(TokenObtainPairView):
	serializer_class = MyTokenObtainPairSerializer

#""""""Auth"""""""""
class SignUp(CreateAPIView):
	serializer_class = SignUpSerializer



#""""""GYM"""""""""
class GymView(ListAPIView):
	queryset =  Gym.objects.all()
	serializer_class = GymSerializer


class CreateGymView(CreateAPIView):
	permission_classes = [IsAuthenticated,IsAdminUser]
	serializer_class = CreateGymSerializer


class UpdateGymView(RetrieveUpdateAPIView):
	queryset =  Gym.objects.all()
	serializer_class = GymUpdateSerializer
	permission_classes = [IsAuthenticated,IsAdminUser]
	lookup_field = 'id'
	lookup_url_kwarg = 'gym_id'


class GymDetailView(ListAPIView):
	lookup_field = "id"
	lookup_url_kwarg = "id"
	# queryset = Gym.objects.get(id=self.kwargs.get("event_id"))
	serializer_class = GymDetailSerializer
	def get_queryset(self):
		gym = Gym.objects.filter(id=self.kwargs.get("id"))
		return gym
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['title', 'type']



#""""""Class"""""""""
class ClassView(ListAPIView):
	queryset =  Class.objects.all()
	serializer_class = ClassSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['title', 'type']


class CreateClassView(CreateAPIView):
	serializer_class = CreateClassSerializer
	permission_classes = [IsAuthenticated,IsAdminUser]



#""""""Booking"""""""""
class BookView(CreateAPIView):
	# book=Booking.objects.get(booking_id=id)
	serializer_class = BookingSerializer
	permission_classes = [IsAuthenticated,]
	def perform_create(self,serializer):
		serializer.save(user=self.request.user)
		book=Booking.objects.get(user=self.request.user)

		send_mail(
					'Booking Confirmation',
					"""This is a automated email to confirm your booking.
					\nReview the below information:\n

					Class Title: %s
					Type:%s
					Date: %s
					Time: %s


					""" % (book.classes.title,book.classes.type,book.classes.date,book.classes.time),
					'ralishteam@gmail.com',
					[self.request.user.email],
					fail_silently=False,
					)


class MyBookings(ListAPIView):
	lookup_field = "id"
	lookup_url_kwarg = "user_id"
	serializer_class = BookingSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Booking.objects.filter(user=self.request.user)


class CancelBooking(DestroyAPIView):
	queryset = Booking.objects.all()
	lookup_field = 'Booking_id'
	lookup_url_kwarg = 'booking_id'
	permission_classes = [IsAuthenticated, IsBookingOwner, IsChangable]
