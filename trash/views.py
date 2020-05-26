from django.shortcuts import render
from django.utils.translation import gettext as _




# Create your views here.
def home(request):
    #from django.utils import translation
    #user_language = 'pl' 
    #translation.activate(user_language)
    #request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    

    #request.session.set_test_cookie()
    #if request.session.test_cookie_worked():
        #print("The test cookie worked!!!")
        #request.session.delete_test_cookie()
    
    #return render(request, 'home.html')


    response = render(request, 'home.html') # store the response in response variable
    if not request.COOKIES.get('cookies_accept'):        
        response.set_cookie('cookies_accept', 'false', 3600 * 24 * 365 * 2)
    
    if not request.COOKIES.get('django_language'):
        response.set_cookie('django_language', 'pl', 3600 * 24 * 365 * 2)

    if not request.COOKIES.get('visits'):        
        response.set_cookie('visits', '1', 3600 * 24 * 365 * 2)
    else:
        visits = int(request.COOKIES.get('visits', '1')) + 1
        response.set_cookie('visits', str(visits),  3600 * 24 * 365 * 2)
    return response