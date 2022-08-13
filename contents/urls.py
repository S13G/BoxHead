from django.urls import path

from contents import views

urlpatterns = [
    path("<int:id>/", views.home, name="home"),
    path("<int:id>/", views.box_map, name="box_map")
]