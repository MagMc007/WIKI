from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entry_page, name="entry_page"),
    path("search/", views.search_page, name="search_page"),
    path("new_page/", views.new_page, name="new_page"),
    path("save/", views.save_new_page, name="save_new_page"),
    path("edit/<str:title>/", views.edit_page, name="edit_page"),
    path("save_page/<str:title>", views.save_page, name="save_page")
]
