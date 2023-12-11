from django.urls import path
from .views import reconocimiento_facial

urlpatterns = [
    path('', reconocimiento_facial, name='reconocimiento'),
]
