from django.urls import path

from contents import views

urlpatterns = [
    path("", views.concept, name='concept'),
    path("box-house/", views.box_house, name="box_house"),
    path("short-term/", views.short_term, name="short_term"),
    path("long-term/", views.long_term, name="long_term"),
    path("box-map/", views.box_map, name="box_map")
]