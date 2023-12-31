"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from homework_4.views import upload_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('', include('games_app.urls')),
    path('', include('homework_1.urls')),
    path('', include('myapp3.urls')),
    path('', include('homework_3.urls')),
    path('', include('myapp4.urls')),
    path('', include('homework_4.urls')),
    path('upload/', upload_image, name='upload_image'),
    # path('__debug__/', include("debug_toolbar.urls")),
]
