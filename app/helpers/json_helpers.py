from django.http import HttpResponseBadRequest, HttpResponse
from bson import ObjectId
import json

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
