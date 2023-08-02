from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_posts>/',
         views.category_post, name='category_posts'),
    path('', views.index, name='index'),
]
