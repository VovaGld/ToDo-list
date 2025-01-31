from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from todo_list.forms import TaskForm
from todo_list.models import Task, Tag


class TagListView(ListView):
    model = Tag
    template_name = "pages/tag_list.html"


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    template_name = "pages/tag_form.html"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "pages/tag_form.html"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


class TaskListView(ListView):
    model = Task
    template_name = "pages/home_page.html"
    context_object_name = "tasks"

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "pages/todo_list-form.html"
    success_url = reverse_lazy("todo_list:home-page")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "pages/todo_list-form.html"
    success_url = reverse_lazy("todo_list:home-page")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:home-page")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


def switch_task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return HttpResponseRedirect(reverse("todo_list:home-page"))
