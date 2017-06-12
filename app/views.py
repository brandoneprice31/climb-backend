from django.http import HttpResponseBadRequest, HttpResponse
from .lib.db import db
import json
from django.views.decorators.csrf import csrf_exempt
from bson import ObjectId

@csrf_exempt
def index(request):
    return HttpResponse("Hello World!")

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


@csrf_exempt
def save_score (request):

    required_fields = ['fb_id', 'score']

    try:
        if request.method != 'POST' or request.content_type != 'application/json':
            raise Exception('request must be POST and application/json')

        data = json.loads(request.body)

        if any(field not in data for field in required_fields):
            raise Exception('incorrect fields')

        fb_id = data['fb_id']
        score = data['score']

        users = db('users')
        user = users.find_one({ 'fb_id' : fb_id })
        if user == None:
            raise Exception("user " + str(fb_id) + " doesn't exist")

        db('scores').insert({   'score' : score,
                                'user' : {
                                    'first_name' : user['first_name'],
                                    'last_name' : user['last_name'],
                                    'fb_id' : user['fb_id']
                                } } )

        return JsonResponse({ 'success' : 'inserted new score' })

    except Exception, e:
        return JsonResponse({ 'error' : str(e) })


@csrf_exempt
def save_user_scores(request):

    required_fields = ['fb_id', 'scores']

    try:
        if request.method != 'POST' or request.content_type != 'application/json':
            raise Exception('request must be POST and application/json')

        data = json.loads(request.body)

        if any(field not in data for field in required_fields):
            raise Exception('incorrect fields')

        fb_id = data['fb_id']
        scores = data['scores']

        users = db('users')
        user = users.find_one({ 'fb_id' : fb_id })
        if user == None:
            raise Exception("user " + str(fb_id) + " doesn't exist")

        score_documents = map( lambda score:
            {
                'score' : score,
                'user' : {
                    'first_name' : user['first_name'],
                    'last_name' : user['last_name'],
                    'fb_id' : user['fb_id']
                }
            }
        , scores)

        db('scores').insert(score_documents)

        return JsonResponse({ 'success' : 'inserted new scores' })

    except Exception, e:
        return JsonResponse({ 'error' : str(e) })


@csrf_exempt
def get_users_scores (request):

    required_fields = ['fb_id']

    try:
        if request.method != 'POST' or request.content_type != 'application/json':
            raise Exception('request must be POST and application/json')

        data = json.loads(request.body)

        if any(field not in data for field in required_fields):
            raise Exception('incorrect fields')

        fb_id = data['fb_id']

        user = db('users').find_one({ 'fb_id' : fb_id })
        if user == None:
            raise Exception("user " + str(fb_id) + " doesn't exist")

        result = list(db('scores').find({ 'user.fb_id' : fb_id } ))
        scores = sorted([score['score'] for score in result], reverse = True)
        result = JSONEncoder().encode({   'success' :   'got users highscores', 'result' : { "scores" :  scores } })

        return JsonResponse(result)

    except Exception, e:
        return JsonResponse({'error' : str(e)})


@csrf_exempt
def get_friends_scores (request):

    required_fields = ['friend_ids']

    try:
        if request.method != 'POST' or request.content_type != 'application/json':
            raise Exception('request must be POST and application/json')

        data = json.loads(request.body)

        if any(field not in data for field in required_fields):
            raise Exception('incorrect fields')

        friend_ids = data['friend_ids']
        friends_scores = db('scores').find({ 'user.fb_id' : { '$in' : friend_ids } }).sort([('score', -1 )])
        result = map(lambda score:
            {   'first_name' : str(score['user']['first_name']),
                'last_name' : str(score['user']['last_name']),
                'fb_id' : str(score['user']['fb_id']),
                'score' : score['score']
            }, friends_scores)
        result = {   'success' :   'got friends highscores', 'result' : { "scores" :  result } }
        return JsonResponse(result)

    except Exception, e:
        return JsonResponse({'error' : str(e)})


@csrf_exempt
def get_global_scores (request):

    try:
        if request.method != 'GET':
            raise Exception('request must be GET')

        scores = db('scores').find({}).sort([('score', -1 )]).limit(100)
        result = map(lambda score:
            {   'first_name' : str(score['user']['first_name']),
                'last_name' : str(score['user']['last_name']),
                'score' : score['score']
            }, scores)
        result = {   'success' :   'got global highscores', 'result' : { "scores" :  result } }
        return JsonResponse(result)

    except Exception, e:
        return JsonResponse({'error' : str(e)})

@csrf_exempt
def get_rank (request):

    required_fields = ['fb_id']

    try:
        if request.method != 'POST' or request.content_type != 'application/json':
            raise Exception('request must be POST and application/json')

        data = json.loads(request.body)

        if any(field not in data for field in required_fields):
            raise Exception('incorrect fields')

        if db('users').find_one({ 'fb_id' : data['fb_id'] }) == None:
            raise Exception('user doesnt exist')


        user_scores = db('scores').find({ 'user.fb_id' : data['fb_id'] }).sort([('score', -1 )])
        if user_scores.count == 0:
            raise Exception('user has no scores')

        users_highest_score = user_scores[0]['score']

        rank = db('scores').find({ 'score' : { '$gt' : users_highest_score } }).count() + 1

        result = {   'success' :   'got rank', 'result' : { "rank" :  rank } }
        return JsonResponse(result)

    except Exception, e:
        return JsonResponse({'error' : str(e)})





def JsonResponse (data):
    data_string = ""
    if not isinstance(data , basestring):
        data_string = str(data).replace("'", '"')
    else:
        data_string = data
    return HttpResponse(data_string, content_type='application/json')



class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
