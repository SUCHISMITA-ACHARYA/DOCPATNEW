from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('<int:patient_id>/', views.patient_profile, name='patient_profile'),
    path('filter-records/', views.filter_records, name='filter_records'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)