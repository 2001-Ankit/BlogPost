from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create/', views.create_blogpost, name='create_blogpost'),
    path('listblog/', views.list_blogposts, name='list_blogposts'),
    path('update/<int:id>/', views.update_blogpost, name='update_blogpost'),
    path('delete/<int:id>/', views.delete_blogpost, name='delete_blogpost'),
    path('',views.list_user,name='dashboard'),
    path('create_user/', views.create_user, name='create_user'),
    path('update_user/<int:id>/', views.update_user, name='update_user'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
    path('category/',views.category_detail,name='category_detail'),
    path('create_category/', views.create_category, name='create_category'),
    path('delete_category/<int:id>/', views.delete_category, name='delete_category'),
    path('update_category/<int:id>/', views.update_category, name='update_category'),
    path('category_blog/<int:category_id>/', views.blogposts_by_category, name='blogposts_by_category'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('specific-categories/', views.show_specific_categories, name='specific_categories'),
]
