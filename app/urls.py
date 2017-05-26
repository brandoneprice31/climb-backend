from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'', index),
    url(r'save_user_score', save_score),
    url(r'users_scores', get_users_scores),
    url(r'save_user_info', save_user_info)
]
