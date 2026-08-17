from django.shortcuts import render
from . models import Fees

# Create your views here.


def fees_list(request):
    
    fees = Fees.objects.all()
    return render(request, "fees/fees_list.html", {"fees":fees})