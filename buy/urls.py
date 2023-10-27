from django.urls import path
from . import views

app_name = 'buy'  # This is an example app name; use your app's name

urlpatterns = [
    path('<int:item_id>/', views.buy_item, name='buy_item'),
]
