from django.shortcuts import render
from django.utils.translation import gettext as _




# Create your views here.
def home(request):
    #from django.utils import translation
    #user_language = 'pl' 
    #translation.activate(user_language)
    #request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return render(request, 'home.html')