"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = 'Index'),
    path('analyze',views.analyze, name = "analyze"),
    # path('analyze',views.analyze, name = "analyze")
    # path('capfirst',views.capfirst, name = "Capitalize First"),
    # path('newlineremove',views.newlineremove, name = "New Line Remover"),
    # path('spaceremove',views.spaceremove, name = "Space Remover"),
]