from rest_framework.routers import DefaultRouter
from .views import MitigationPlanViewSet

router = DefaultRouter()
router.register(r"plans", MitigationPlanViewSet, basename="mitigationplan")

urlpatterns = router.urls
