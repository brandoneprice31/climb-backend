from ..db.db import db
import json
from ..helpers.json_helpers import *
from django.views.decorators.csrf import csrf_exempt
from bson import ObjectId

@csrf_exempt
def get_user_info(request):
    required_fields = ['fb_id']

    try:
        if request.method != 'POST' or request.content_type != 'application/json':
            raise Exception('request must be POST and application/json')

        data = json.loads(request.body)

        if any(field not in data for field in required_fields):
            raise Exception('incorrect fields')

        user = db('users').find_one({ 'fb_id' : data['fb_id'] })
        if user == None:
            raise Exception('user doesnt exist')

        result = JSONEncoder().encode({ 'success' : 'got user information', 'result' :  { 'user' : user } })
        return JsonResponse(result)

    except Exception, e:
        return JsonResponse({'error' : str(e)})


@csrf_exempt
def create_user (request):
    required_fields = ['first_name', 'last_name', 'fb_id']

    try:
        if request.method != 'POST' or request.content_type != 'application/json':
            raise Exception('request must be POST and application/json')

        data = json.loads(request.body)

        if any(field not in data for field in required_fields):
            raise Exception('incorrect fields')

        if db('users').find_one({ 'fb_id' : data['fb_id'] }) != None:
            raise Exception('user already exists')

        user = {
                'fb_id' : data['fb_id'],
                'first_name' : data['first_name'],
                'last_name' : data['last_name'],
                'coins' : 0,
                'sprites' : {
                    'climber' : [],
                    'spikeball' : []
                },
                'extra_lives' : 0,
                'ads' : True
        }

        db('users').insert(user)
        result = JSONEncoder().encode({ 'success' : 'saved user information', 'result' :  { 'user' : user } })
        return JsonResponse(result)

    except Exception, e:
        return JsonResponse({'error' : str(e)})


@csrf_exempt
def save_user_info (request):

    required_fields = ['fb_id']

    try:
        if request.method != 'POST' or request.content_type != 'application/json':
            raise Exception('request must be POST and application/json')

        data = json.loads(request.body)

        if any(field not in data for field in required_fields):
            raise Exception('incorrect fields')

        fb_id = data['fb_id']

        if db('users').find_one({ 'fb_id' : fb_id }) == None:
            raise Exception('user doesnt exist')

        new_data = {}

        # Sprites.
        if 'sprites' in data:
            sprites = data['sprites']
            if 'climber' in sprites:
                new_data['sprites.climber'] = sprites['climber']
            if 'spikeball' in sprites:
                new_data['sprites.spikeball'] = sprites['spikeball']

        # Extra lives.
        if 'extra_lives' in data:
            new_data['extra_lives'] = data['extra_lives']

        # Ads.
        if 'ads' in data:
            new_data['ads'] = data['ads']

        # Coins.
        if 'coins' in data:
            new_data['coins'] = data['coins']

        db('users').update_one({ 'fb_id' : fb_id }, {'$set' : new_data} )
        user = db('users').find_one({ 'fb_id' : fb_id })
        result = JSONEncoder().encode({ 'success' : 'updated user info', 'result' : { 'user' : user } })

        return JsonResponse(result)

    except Exception, e:
        return JsonResponse({ 'error' : str(e) })
