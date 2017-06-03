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

        if 'fb_id' in data and db('users').find_one({ 'fb_id' : data['fb_id'] }) != None:
            new_data = { key : data[key] for key in data.keys() if key != 'fb_id' }
            db('users').update({ 'fb_id' : data['fb_id'] }, new_data)
            return JsonResponse({ 'success' : 'updated user information' })

        db('users').insert(data)
        return JsonResponse({ 'success' : 'saved user information' })

    except Exception, e:
        return JsonResponse({'error' : str(e)})


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

        db('scores').insert({ 'score' : score, 'user' : user } )

        return JsonResponse({ 'success' : 'inserted new score' })

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

        user_id = data['fb_id']

        user = db('users').find_one({ 'fb_id' : fb_id })
        if user == None:
            raise Exception("user " + str(fb_id) + " doesn't exist")

        result = list(db('scores').find({ 'user.fb_id' : fb_id } ))
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
