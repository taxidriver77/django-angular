from scrumboard.views import ListViewSet,CardViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lists', ListViewSet, r"lists")
router.register(r'cards', CardViewSet, r"cards")

urlpatterns = router.urls
