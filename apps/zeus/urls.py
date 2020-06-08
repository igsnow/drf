from rest_framework.routers import DefaultRouter
from apps.zeus import views

router = DefaultRouter()
router.register(r'hello', views.HelloWorldViewSet, basename="hello")
urlpatterns = router.urls
