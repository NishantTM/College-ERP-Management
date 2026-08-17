from django.shortcuts import render
from . models import Result

# Create your views here.


def result_list(request):
    
    result = Result.objects.all()
    return render(request, "results/result_list.html", {"result": result})