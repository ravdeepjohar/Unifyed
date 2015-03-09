from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from unifyed_signup.models import Person
# Create your views here.
from django.http import HttpResponse
from unifyed_signup.forms import SignupForm

def index(request):
    
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():            
            signup = form.save(commit=True)            
        return redirect('response.html')

    return render_to_response('index.html', {'form':form}, context_instance=RequestContext(request))


def response(request):
    
    return render(request,'response.html', {})