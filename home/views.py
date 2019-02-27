from django.shortcuts import render, redirect

# Create your views here.

from .models import Jugador
from .forms import FormJugador

from .models import Equipo
from .forms import FormEquipo

from .models import Estadio
from .forms import FormEstadio

from .filters import UserFilter
from .filters2 import UserFilter2

def  index(request):
	return render(request, "home/index.html")


def  jugador(request):
	queryset = Jugador.objects.all() 
	context = {
	"objects": queryset

	}
	return render(request, "home/jugador.html", context)



def createJ(request):
		form = FormJugador(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect('jugador')
		else:
			form = FormJugador()

		context= {

		"form": form

		}
		return render(request, "home/createJ.html", context)


def  equipos(request):
	queryset = Equipo.objects.all() 
	context = {
	"objects": queryset

	}
	return render(request, "home/equipos.html", context)


def createE(request):
		form = FormEquipo(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect('equipos')
		else:
			form = FormEquipo()

		context= {

		"form": form

		}
		return render(request, "home/createE.html", context)


def  estadio(request):
	queryset = Estadio.objects.all() 
	context = {
	"objects": queryset

	}
	return render(request, "home/estadio.html", context)


def createEst(request):
		form = FormEstadio(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect('estadio')
		else:
			form = FormEstadio()

		context= {

		"form": form

		}
		return render(request, "home/createEst.html", context)


def updateJ(request, id):
	object_Jugador = Jugador.objects.get(id=id)
	if request.method == "GET":
		form = FormJugador(instance=object_Jugador)
	else:
		form = FormJugador(request.POST, instance=object_Jugador)
		if form.is_valid():
			form.save()    #guarda el cuando se llenan todos los campos
			return redirect("jugador")
	context = {
			"form": form

			  }
	return render(request, "home/updateJ.html", context)


def updateEst(request, id):
	object_Estadio = Estadio.objects.get(id=id)
	if request.method == "GET":
		form = FormEstadio(instance=object_Estadio)
	else:
		form = FormEstadio(request.POST, instance=object_Estadio)
		if form.is_valid():
			form.save()    #guarda el cuando se llenan todos los campos
			return redirect("estadio")
	context = {
			"form": form

			  }
	return render(request, "home/updateEst.html", context)


def updateE(request, id):
	object_Equipo = Equipo.objects.get(id=id)
	if request.method == "GET":
		form = FormEquipo(instance=object_Equipo)
	else:
		form = FormEquipo(request.POST, instance=object_Equipo)
		if form.is_valid():
			form.save()    #guarda el cuando se llenan todos los campos
			return redirect("equipos")
	context = {
			"form": form

			  }
	return render(request, "home/updateE.html", context)



def detailJ(request, id):
	queryset = Jugador.objects.filter(id=id)
	context = {
		"objects": queryset
	}

	return render(request, "home/detailJ.html", context)


def detailE(request, id):
	queryset = Equipo.objects.filter(id=id)
	context = {
		"objects": queryset
	}

	return render(request, "home/detailE.html", context)


def detailEst(request, id):
	queryset = Estadio.objects.filter(id=id)
	context = {
		"objects": queryset
	}

	return render(request, "home/detailEst.html", context)


def search(request):
    user_list = Jugador.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'home/search.html', {'filter': user_filter})


def searchE(request):
    user_list = Jugador.objects.all()
    user_filter = UserFilter2(request.GET, queryset=user_list)
    return render(request, 'home/searchE.html', {'filter': user_filter})


