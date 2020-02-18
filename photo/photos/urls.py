from rest_framework.routers import DefaultRouter

from photo.photos import views

app_name = 'photos'

router = DefaultRouter()
router.register(r'photos', views.PhotosViewset, basename='photos')


urlpatterns = router.urls
