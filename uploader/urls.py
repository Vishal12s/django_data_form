from django.urls import path
from .views import upload_file, generate_report, home

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_file, name='upload_file'),
    path('report/', generate_report, name='generate_report'),
]