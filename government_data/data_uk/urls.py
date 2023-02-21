from django.contrib import admin
from django.urls import path, include
from data_uk import views

urlpatterns = [
    path('', views.getPrice, name="get_data"),
]
    # path('data/<int:id>/', views.data_detail, name="data_detail")
# ]urlpatterns = [
#     path('', views.get_data, name="get_data"),
#     path('data/<int:id>/', views.data_detail, name="data_detail")
# ]
