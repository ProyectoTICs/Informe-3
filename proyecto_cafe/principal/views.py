from django.shortcuts import render
from django.shortcuts import render_to_response
   def lista_trabajadores(request):
    trabajadores = Trabajador.objects.all()
    return render_to_response('lista_trabajadores.html',{'lista':trabajadores})
# Create your views here.
