from rest_framework.routers import DefaultRouter
from .views import SecurityViewSet

router = DefaultRouter()
router.register(r"securities", SecurityViewSet, basename="security")

urlpatterns = router.urls
