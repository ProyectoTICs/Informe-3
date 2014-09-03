from django.shortcuts import render
from django.shortcuts import render_to_response , get_object_or_404
from django.contrib.auth.models import User
from principal.models import Trabajador, Cafe   
from django.http import HttpResponse, HttpResponseRedirect
from principal.forms import TrabajadorForm
def lista_trabajadores(request):
	trabajador = Trabajador.objects.all()
	return render_to_response('inicio.html',{'lista':trabajador})

def lista_cafe(request):
	cafe = Cafe.objects.all()
	return render_to_response('lista_trabajadores.html',{'cafes':cafe})
# Create your views here.
def nuevo_trabajador(request):
	if request.method == 'POST':
		formulario = TrabajadorForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/agregar')
	else:
		formulario = TrabajadorForm()

	return render_to_response('trabajadorform.html',{'formulario':formulario},context_instance=RequestContext(request))