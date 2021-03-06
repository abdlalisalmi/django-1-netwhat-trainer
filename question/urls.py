"""web_netwhat_trainer URL Configuration

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

from django.urls import path
from .views import (
    question_view,
    repons_handle,
    result_view,
)

app_name = 'question'

urlpatterns = [
    path('<str:language>/<int:id>/', question_view, name='question_view'),
    path('<str:language>/<int:id>/repons_handel', repons_handle, name='repons_handle'),
    path('<str:language>/result/', result_view, name='result')
]
