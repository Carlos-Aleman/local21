from django.contrib.auth.models import User
import django_filters
from .models import Jugador

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Jugador
        fields = [
        	'posicion',
 ]



class UserFilterE(django_filters.FilterSet):
    class Meta:
        model = Jugador
        fields = [
        	'equipo',
 ]