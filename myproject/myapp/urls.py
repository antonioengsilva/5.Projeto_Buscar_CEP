# myapp/urls.py

from django.urls import path
from .views import ConsulteCEPView

urlpatterns = [
    path('', ConsulteCEPView.as_view(), name='consulte-cep-view'),
]
