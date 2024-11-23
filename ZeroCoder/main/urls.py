from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('game/', views.game, name='games'),
    path('suppliers/', views.suppliers, name='suppliers'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy'),
    path('terms-of-service/', views.terms_of_service, name='terms'),

]