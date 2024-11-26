from django.contrib import admin
from django.urls import path, re_path

from common import views as common_views

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^__version__/?$', common_views.version),
]
