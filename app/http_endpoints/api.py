from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from .scores import *
from .users import *

@csrf_exempt
def index(request):
    return HttpResponse("Waddup homes")

url_method_map = [
    url(r'^$', index),
    url(r'^save_score$', save_score),
    url(r'^get_users_scores$', get_users_scores),
    url(r'^create_user$', create_user),
    url(r'^get_user_info$', get_user_info),
    url(r'^save_user_info$', save_user_info),
    url(r'^get_friends_scores$', get_friends_scores),
    url(r'^get_global_scores$', get_global_scores),
    url(r'^get_rank$', get_rank),
    url(r'^save_user_scores$', save_user_scores)
]
