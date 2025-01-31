from django.test import TestCase
from django.urls import reverse

from todo_list.models import Tag, Task

HOME_PAGE_URL = reverse("todo_list:home-page")


class TestTodoView(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name='tag1')

        self.test_task1 = Task.objects.create(
            content='test task1',
        )
        self.test_task1.tags.add(self.tag1)

        self.test_task2 = Task.objects.create(
            content='test task2',
        )
        self.test_task2.tags.add(self.tag1)


    def test_ordering_task_by_date(self):
        response = self.client.get(HOME_PAGE_URL)
        self.assertEqual(list(response.context["tasks"])[0], self.test_task2)

    def test_ordering_task_by_complete(self):
        test_task = Task.objects.create(
            content='test task',
            done=True,
        )
        test_task.tags.add(self.tag1)
        resource = self.client.get(HOME_PAGE_URL)
        self.assertEqual(list(resource.context["tasks"])[-1], test_task)

    def test_task_complete(self):

        url = reverse("todo_list:task-complete", kwargs={"pk": self.test_task1.id})
        response = self.client.get(url)

        self.test_task1.refresh_from_db()
        self.assertEqual(self.test_task1.done, True)
        self.assertRedirects(response, HOME_PAGE_URL)

        response = self.client.get(url)
        self.test_task1.refresh_from_db()

        self.assertEqual(self.test_task1.done, False)
        self.assertRedirects(response, HOME_PAGE_URL)
