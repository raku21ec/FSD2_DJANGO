from django.urls import path
from . import views

urlpatterns = [
    path('', views.layout, name='layout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('book/', views.book_ticket, name='book_ticket'),
    path('success/', views.success, name='success'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]