from django.urls import path
from snippets import views

urlpatterns = [
path('', views.create, name = 'create'),
path('view/<int:key>/', views.view, name = 'view')
]
