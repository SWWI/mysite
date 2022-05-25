from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
from django.shortcuts import render
from .models import Question
# ef index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'swwi': latest_question_list,
#         'hello': 'World'
#     }
#     return HttpResponse(template.render(context, request))
last  = Question.object.first()
context = {
    'obj': last
}
return render(request "polls/index.html", context)