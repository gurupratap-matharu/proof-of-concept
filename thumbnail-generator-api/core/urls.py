from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework import routers

from core.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'profile/photos', views.ProfileViewSet)

# initialize schema for server side documentation
schema_view = get_schema_view(title='Thumbnail API',
                              description='An API that generates thumbnails for users in 3 different formats.')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='Thumbnail Generator API'))
]
