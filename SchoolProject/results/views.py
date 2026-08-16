from django.shortcuts import render

# Create your views here.


def result_list(request):
    return render(request, "fees/result_list.html")