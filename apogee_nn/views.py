from django.shortcuts import render

from django.http import HttpResponse
from .models import Target
import numpy


NOF_OBJECTS = len(Target.objects.all())
PATH = 'apogee_nn/'




def neighbors(request, target_id):
    response = "Nearest neighbors of APOGEE ID %s:"
    target_object = Target.objects.filter(id = target_id)
    response = response % target_object[0]
    response = response + '<br/>'

    for neighbor in target_object[0].neighbor_set.all():
        response = response + str(neighbor.neighbor_rank) + ':                ' + neighbor.neighbor_id + '<br/>'

    return HttpResponse(response)




def index(request):
    nof_objects = len(Target.objects.all())
    random_inds = numpy.random.choice(numpy.arange(nof_objects-1), 10) + 1
    #print(random_inds)
    #random_inds = random_inds.astype(int)
    #target_list = Target.objects.all()[random_inds]
    target_list = [Target.objects.get(id = idx) for idx in random_inds]
    context = {'target_list': target_list}
    return render(request, PATH + 'index.html', context)

def detail(request, target_id):
    try:
        target = Target.objects.get(target_id=target_id)
    except Target.DoesNotExist:
        raise Http404("APOGEE ID does not exist in our dataset")
    return render(request, PATH + 'detail.html', {'target': target})


from django.core.exceptions import *

def form(request):
    return render(request, PATH + 'form.html')

def search(request):
    if request.method == 'POST':
        user_input = request.POST.get('textfield', None)
        #print(user_input)
        try:
            #filter(headline__startswith
            #target = Target.objects.get(pk=target_id)
            #return render(request, PATH + 'detail.html', {'target': target})

            target_list = Target.objects.filter(target_id__startswith = user_input)
            context = {'target_list': target_list}
            return render(request, PATH + 'index.html', context)
        except Target.DoesNotExist:
            raise Http404("APOGEE ID does not exist in our dataset")
    else:
        return render(request, PATH + 'form.html')