from django.shortcuts import render
from django.utils.translation import gettext as _

# Create your views here.
def home(request):
    return render(request, 'home.html')