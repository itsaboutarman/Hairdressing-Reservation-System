from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.get_stylists, name='posts_list'),
    path('posts/<int:stylist_id>/', views.get_stylist, name='stylist_detail'),
    path('my-details/', views.stylist_view, name='stylist_page'),
]
