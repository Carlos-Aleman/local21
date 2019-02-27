"""nflp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from home import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.index, name="index"),

    path('jugador/', views.jugador, name="jugador"),

    path('detailJ/<int:id>/', views.detailJ, name="detailJ"),

    path('detailE/<int:id>/', views.detailE, name="detailE"),

    path('detailEst/<int:id>/', views.detailEst, name="detailEst"),

    path('createJ/', views.createJ, name="createJ"),

    path('equipos/', views.equipos, name="equipos"),

    path('createE/', views.createE, name="createE"),

    path('estadio/', views.estadio, name="estadio"),

    path('createEst/', views.createEst, name="createEst"),

    path('updateJ/<int:id>/', views.updateJ, name="updateJ"),

    path('updateEst/<int:id>/', views.updateEst, name="updateEst"),

    path('updateE/<int:id>/', views.updateE, name="updateE"),

    path('search/', views.search, name='search'),

    path('searchE/', views.searchE, name='searchE'),

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
