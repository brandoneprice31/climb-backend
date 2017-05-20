from django.conf.urls import url, include
from views import save_score, get_users_scores

urlpatterns = [
    url(r'save_user_score', save_score),
    url(r'users_scores', get_users_scores)
]
