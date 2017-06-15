from ..db.db import db
import json
from ..helpers.json_helpers import *
from django.views.decorators.csrf import csrf_exempt
from bson import ObjectId

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

        result = db('scores').find({ 'user.fb_id' : fb_id } ).sort([('score', -1 )]).limit(100)
        scores = map(lambda score: score['score'], result)
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
        result = GetTop100DistinctScores(friends_scores)
        result = {   'success' :   'got friends highscores', 'result' : { "scores" :  result } }
        return JsonResponse(result)

    except Exception, e:
        return JsonResponse({'error' : str(e)})


@csrf_exempt
def get_global_scores (request):

    try:
        if request.method != 'GET':
            raise Exception('request must be GET')

        scores = db('scores').find({}).sort([('score', -1 )])
        result = GetTop100DistinctScores(scores)
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

        scores_higher = db('scores').find({ 'score' : { '$gt' : users_highest_score } })
        distinct_fb_id = set()
        for score in scores_higher:
            if score['user']['fb_id'] not in distinct_fb_id:
                distinct_fb_id.add(score['user']['fb_id'])

        rank = len(distinct_fb_id) + 1
        result = {   'success' :   'got rank', 'result' : { "rank" :  rank } }
        return JsonResponse(result)

    except Exception, e:
        return JsonResponse({'error' : str(e)})




def GetTop100DistinctScores(scores):
    fb_ids = set()
    top100 = []

    for score in scores:
        if score['user']['fb_id'] in fb_ids:
            continue

        top100.append({
            'first_name' : str(score['user']['first_name']),
            'last_name' : str(score['user']['last_name']),
            'score' : score['score']
        })
        fb_ids.add(score['user']['fb_id'])

        if len(top100) == 100:
            break

    return top100
