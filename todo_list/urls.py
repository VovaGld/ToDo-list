from django.urls import path

from todo_list.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    switch_task_complete,
    TagListView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="home-page"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/update/<int:pk>", TaskUpdateView.as_view(), name="task-update"),
    path("task/delete/<int:pk>", TaskDeleteView.as_view(), name="task-delete"),
    path("task/comlete/<int:pk>", switch_task_complete, name="task-complete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo_list"
