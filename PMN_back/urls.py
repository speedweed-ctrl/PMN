
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="PMN api endponits",
      default_version='dev',
      description="the api endponts for the password managment app",
   ),
    #this 2 lines if removed wiill hide some endponits
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('',schema_view.with_ui()),
    # path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls'))

]


