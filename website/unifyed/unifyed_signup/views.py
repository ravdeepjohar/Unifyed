from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from unifyed_signup.models import Person
# Create your views here.
from django.http import HttpResponse
from forms import SingupForm

def index(request):
	# A HTTP POST?
    if request.method == 'POST':
        form = SingupForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return response(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors

    else:
        # If the request was not a POST, display the form to enter details.
        form = SignupForm()


    return render(request, 'index.html', {'form':form})


def response(request):
    #context = RequestContext(request)
    return render(request,'response.html', {})