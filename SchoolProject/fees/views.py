from django.shortcuts import render

# Create your views here.


def fees_list(request):
    return render(request, "fees/fees_list.html")