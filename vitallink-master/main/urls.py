from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from users import views as v
urlpatterns =[
    path("",views.index, name="index"),
    path("Type-of-Login /", views.choose, name = 'choose'),
    path("Home/", views.index, name = 'home'),

    path("Patient-Registeration/", v.patient_information, name='patient_information'),
    path("Patient-Registeration-Page-2/", v.record_submit, name='record_submit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
