

from django.urls import path,include
from . import views
urlpatterns = [
  path("",views.create,name="create"),
  path("list/",views.list,name="list"),
  path("edit/",views.edit,name="edit")
]
