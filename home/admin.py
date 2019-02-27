from django.contrib import admin

# Register your models here.


from .models import Jugador
from .models import Equipo
from .models import Estadio

admin.site.register(Jugador)
admin.site.register(Equipo)
admin.site.register(Estadio)