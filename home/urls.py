from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("article/<slug:slug>", views.article, name="article"),
    path("delete/<slug:slug>", views.delete_article, name="delete"),
    path("update/<slug:slug>", views.update_article, name="update"),
    path("profile/", views.userProfile, name="userProfile"),
    path("delete-comment/<int:id>", views.delete_comment, name="delete-comment"),
]
