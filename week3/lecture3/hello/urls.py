from django.urls import path
from . import views

urlpatterns =[
       path("",views.index,name="index"),
       path("<str:name>",views.greet,name="greet"),
      path("Pranjul",views.Pranjul,name="Pranjul"),
      path("david",views.david,name="david")



]