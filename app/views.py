from django.http import HttpResponseBadRequest, HttpResponse
from .lib.db import db
import json
from django.views.decorators.csrf import csrf_exempt
from bson import ObjectId

@csrf_exempt
def index(request):
    return HttpResponse("Hello World!")

@csrf_exempt
def save_user_info (request):
    required_fields = []

    try:
        if request.method != 'POST' or request.content_type != 'application/json':
            raise Exception('request must be POST and application/json')

        data = json.loads(request.body)

        if any(field not in data for field in required_fields):
            raise Exception('incorrect fields')

        if 'user_id' in data:
            new_data = { key : data[key] for key in data.keys() if key != 'user_id' }
            db('users').update({ '_id' : ObjectId(data['user_id']) }, new_data)
            return JsonResponse({ 'success' : 'updated user information' })

        if 'fb_id' in data and db('users').find_one({ 'fb_id' : data['fb_id'] }) != None:
            raise Exception('fb id already exists')

        user_id = str(db('users').insert(data))
        return JsonResponse({ 'success' : 'saved user information', 'result' : { 'user_id' : user_id } })

    except Exception, e:
        return JsonResponse({'error' : str(e)})


@csrf_exempt
def save_score (request):

    required_fields = ['user_id', 'score']

    try:
        if request.method != 'POST' or request.content_type != 'application/json':
            raise Exception('request must be POST and application/json')

        data = json.loads(request.body)

        if any(field not in data for field in required_fields):
            raise Exception('incorrect fields')

        user_id = ObjectId(data['user_id'])
        score = data['score']

        users = db('users')
        user = users.find_one({ '_id' : user_id })
        if user == None:
            raise Exception("user " + str(user_id) + " doesn't exist")

        db('scores').insert({ 'score' : score, 'user' : user } )

        return JsonResponse({ 'success' : 'inserted new score' })

    except Exception, e:
        return JsonResponse({ 'error' : str(e) })

@csrf_exempt
def get_users_scores (request):

    required_fields = ['user_id']

    try:
        if request.method != 'POST' or request.content_type != 'application/json':
            raise Exception('request must be POST and application/json')

        data = json.loads(request.body)

        if any(field not in data for field in required_fields):
            raise Exception('incorrect fields')

        user_id = ObjectId(data['user_id'])

        user = db('users').find_one({ '_id' : user_id })
        if user == None:
            raise Exception("user " + str(user_id) + " doesn't exist")

        result = list(db('scores').find({ 'user._id' : user_id } ))
        scores = sorted([score['score'] for score in result], reverse = True)
        result = JSONEncoder().encode({   'success' :   'got users highscores', 'result' : { "scores" :  scores } })

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
