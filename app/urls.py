from django.contrib import admin
from django.urls import path, re_path

from app.common import views as common_views
from app.cocktail import views as cocktail_views

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^__version__/?$', common_views.version),

    re_path(r'^', cocktail_views.index_view, name='index'),
]
