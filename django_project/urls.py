"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from appzinho import views

urlpatterns = [
  path('', views.homepage, name="home"),
  path('top-movies', views.top_movies),
  path('top-movies/update/<id>', views.update_top_movies),
  path('top-movies/delete/<id>', views.delete_top_movies),
  path('movies', views.movies),
  path('movies/update/<id>', views.update_movies),
  path('movies/delete/<id>', views.delete_movies),
  path('admin/', admin.site.urls),
]
