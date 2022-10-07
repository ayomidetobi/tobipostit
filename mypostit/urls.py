from django.urls import path,include
from .views import indexView,post_detail,profile,update_view,article_view,delete_view
from . import views
urlpatterns = [
    path('',indexView.as_view(template_name = 'index.html'),name='index'),
    path('story/',views.story,name='story'),
    path('', include("django.contrib.auth.urls")),
    path('signup/',views.signup_page,name='signup'),
    path('login_user/',views.login_user,name='login_user'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('profile/followers_count',views.follwers_count,name='followers_count'),
    path('logout/',views.logout,name='logout'),
    path('post_detail/', post_detail.as_view(),name='post_detail'),
    path('accounts/', include('allauth.urls')),
    path('profile/update/<int:pk>', update_view.as_view(),name='update_view'),
    path('article/<int:pk>', article_view.as_view(),name='article_view'),
    path('profile/delete/<int:pk>', delete_view.as_view(),name='delete_view')

    
]
