from django.urls import path
from .views import *
urlpatterns =[

    path("", ListlistView.as_view(), name="index"),
    path("list/<int:list_id>/", itemListView.as_view(), name="list"),
    # CRUD patterns for ToDoLists
    path("list/add/",ListCreate.as_view(), name="list-add"),
    path(
        "list/<int:pk>/delete/", ListDelete.as_view(), name="list-delete"
    ),
    # CRUD patterns for ToDoItems
    path(
        "list/<int:list_id>/item/add/",
        ItemCreate.as_view(),
        name="item-add",
    ),
    path(
        "list/<int:list_id>/item/<int:pk>/",
        ItemUpdate.as_view(),
        name="item-update",
    ),
    path(
        "list/<int:list_id>/item/<int:pk>/delete/",
        ItemDelete.as_view(),
        name="item-delete",
    ),
    path(
        'list/<int:list_id>/edit',ListUpdate.as_view(),name='list-edit'
    )
]