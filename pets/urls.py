from django.urls import path
from .views import PetView, PetParamView


urlpatterns = [
    path('pets', PetView.as_view()),
    path('pets/<int:pet_id>', PetParamView.as_view())
]
