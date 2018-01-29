# Create your views here.

from django.shortcuts import render_to_response 
from sentence_of_the_day_app.models import sentences
 
def home(request):
    sentence = sentences.objects.all()[0]
    return render_to_response('index.html', {'sentence' : sentence})
