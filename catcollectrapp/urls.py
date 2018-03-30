from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # re_path(r'^([0-9]+)/$', views.show, name='show'),
    path('<int:cat_id>/', views.show, name='show'),
    path('post_cat/', views.post_cat, name='post_cat'),
    path('user/<user_name>', views.profile, name='profile'),
]
