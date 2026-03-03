from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_users, name="list_users"),
    path("create/", views.create_user, name="create_user"),
    path("<uuid:user_id>/", views.get_user, name="get_user"),
    path("<uuid:user_id>/update/", views.update_user, name="update_user"),
    path("<uuid:user_id>/delete/", views.delete_user, name="delete_user"),
]
