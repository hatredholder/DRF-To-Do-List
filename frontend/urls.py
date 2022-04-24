from django.urls import include, path

from .views import list

urlpatterns = [
    path('', list, name='list')
]
