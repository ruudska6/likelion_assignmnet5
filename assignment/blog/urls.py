from . import views
from django.urls import path
from . import views
urlpatterns = [
    path('blog/create', views.create, name='create'),
    path('blog/<int:blog_id>', views.detail, name ='detail'),
    path('blog/list/', views.blog_list, name='list')
]
