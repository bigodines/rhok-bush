from django.shortcuts import render_to_response
from forms import CallForm

def cadastro(request):

    call_form = CallForm()

    return render_to_response('volunteers/calls/new.html', {'form': call_form})

