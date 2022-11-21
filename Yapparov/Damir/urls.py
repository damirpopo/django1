from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, kwargs={'name': 'Яппаров Дамир Рамильевич', 'age': 18, "interests": 'computer'}, name="home"),
    path("about",views.about),
    path("contacts",views.contacts),
]