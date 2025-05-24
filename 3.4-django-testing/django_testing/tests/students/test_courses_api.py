from django.urls import reverse
import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from students.models import Course


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(**kwargs):
        return baker.make(Course, **kwargs)
    return factory


@pytest.mark.django_db
def test_retrieve_course(api_client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', args=[course.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == course.id

    assert response.data['name'] == course.name


@pytest.mark.django_db
def test_filter_id(api_client, course_factory):
    courses = course_factory(_quantity=3)
    target = courses[1]
    url = reverse('courses-list')
    response = api_client.get(url, data={'id': target.id})
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['id'] == target.id


@pytest.mark.django_db
def test_filter_name(api_client, course_factory):
    course_factory(name="Django Course")
    course_factory(name="Python Course")
    url = reverse('courses-list')
    response = api_client.get(url, data={'name': 'Django Course'})
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Django Course'


@pytest.mark.django_db
def test_create_course(api_client):
    url = reverse('courses-list')
    data = {'name': 'New Course'}
    response = api_client.post(url, data=data)
    assert response.status_code == 201
    assert Course.objects.filter(name='New Course').exists()


@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    course = course_factory(name="Initial")
    url = reverse('courses-detail', args=[course.id])
    response = api_client.patch(url, data={'name': 'Updated'})
    assert response.status_code == 200
    course.refresh_from_db()
    assert course.name == 'Updated'


@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', args=[course.id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not Course.objects.filter(id=course.id).exists()

