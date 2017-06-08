from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^save_score$', save_score),
    url(r'^get_users_scores$', get_users_scores),
    url(r'^create_user$', create_user)
]
