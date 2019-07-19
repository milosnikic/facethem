from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('facethemapp/developer', views.developer, name='developer'),
    path('facethemapp/friends', views.friends, name='friends'),
    path('facethemapp/latestmatches', views.latest_matches, name='latest_matches'),
    path('facethemapp/login', views.login_user, name='login'),
    path('facethemapp/profile/<str:username>', views.profile, name='profile'),
    path('facethemapp/register', views.register, name='register'),
    path('facethemapp/search', views.search, name='search'),
    path('facethemapp/settings', views.settings, name='settings'),
    path('facethemapp/about', views.about, name='about'),
    path('facethemapp/stats', views.stats, name='stats'),
    path('facethemapp/<str:username>/friends', views.friends_profile, name='friends_profile'),
    path('facethemapp/logout', views.logout_user, name='logout_user'),
]
