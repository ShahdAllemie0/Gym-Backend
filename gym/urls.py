from django.contrib import admin
from django.urls import path
from gyms import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
# """""Auth""""""""
    path('api/login/', TokenObtainPairView.as_view(), name='api-login'),
    path('api/signup/', views.SignUp.as_view(), name='api-signup'),

#""""""GYM"""""""""
    path('api/gym/', views.GymView.as_view(), name='api-event'),
    path('api/gymcreate/', views.CreateGymView.as_view(), name='api-create'),
    path('api/update/gym/<int:gym_id>/', views.UpdateGymView.as_view(), name='api-update-even'),

#""""""Class"""""""""
    path('api/class/', views.ClassView.as_view(), name='api-class'),
    path('api/class/create/', views.CreateClassView.as_view(), name='api-create-class'),

#""""""Booking"""""""""
    path('api/book/', views.BookView.as_view(), name='api-booking'),
    path('api/mybooking/', views.MyBookings.as_view(), name='api-mybooking'),
    path('api/cancel/<int:booking_id>/', views.CancelBooking.as_view(), name="api-cancel-booking"),

]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
