from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter() # amader router

router.register(r'', views.AppointmentViewSet) 

urlpatterns = [
]+ router.urls