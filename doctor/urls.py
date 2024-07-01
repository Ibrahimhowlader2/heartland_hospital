from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register(r'list', views.DoctorViewset) # router er antena
router.register(r'specialization', views.SpecializationViewset) # router er antena
router.register(r'available_time', views.AvailableTimeViewset) # router er antena
router.register(r'designation', views.DesignationViewset) # router er antena
router.register(r'reviews', views.ReviewViewset) # router er antena

urlpatterns = [
]+ router.urls