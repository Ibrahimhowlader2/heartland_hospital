from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register(r'', views.ServiceViewset) # router er antena
urlpatterns = [
]+ router.urls