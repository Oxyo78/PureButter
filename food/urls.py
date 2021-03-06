from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/<str:search>',views.result, name='result'),
    path('product/', views.product, name='product'),
    path('product/<int:number>', views.product, name='product'),
    path('account/', views.account, name='account'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('save/<str:search>/<int:number>', views.save, name='save'),
    path('legal', views.legal, name='legal'),
]
