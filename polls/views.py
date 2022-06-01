from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
from django.shortcuts import render
from .models import Question
from .models import Carousel
# ef index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'swwi': latest_question_list,
#         'hello': 'World'
#     }
#     return HttpResponse(template.render(context, request))
def index(request):
    items = Carousel.objects.all()
    # last  = Question.objects.first()
    # context = {
    #     'obj': last
    # }
    return render(request, "home.html", {'obj_list': items})

def about(request):
    return render(request, "index.html", {})

def contact(request):
    return render(request, "contact.html", {})