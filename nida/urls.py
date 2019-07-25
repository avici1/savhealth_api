from django.urls import path

from .views import PersonView,InsuranceView

app_name = "nida"

# app_name for reverse lookup

urlpatterns = [
    path('persons/<str:fPd>',PersonView.as_view()),
    path('insurance/<str:fPd>',InsuranceView.as_view()),
    path('med/<str:fPd>',InsuranceView.as_view())
]