from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import CallForm
from models import Call

def cadastro(request):

    context = {}
    context.update(csrf(request))

    if request.method == 'POST': # If the form has been submitted...
        call_form = CallForm(request.POST) # A form bound to the POST data
        if call_form.is_valid(): # All validation rules pass

            call_form.save()

            return HttpResponseRedirect('/bush/chamada/%s' % call_form.cleaned_data['slug']) # Redirect after POST
    else:
        call_form = CallForm() # An unbound form

    context['form'] = call_form
    return render_to_response('volunteers/calls/new.html', context)

