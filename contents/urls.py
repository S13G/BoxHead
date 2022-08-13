from django.urls import path

from contents import views

urlpatterns = [
    path("<int:id>/", views.home, name="home"),
]