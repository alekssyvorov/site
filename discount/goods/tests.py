from django.test import TestCase  # noqa: F401
from goods.models import Register  # noqa: F401
import pytest


@pytest.mark.urls("goods/urls")
def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.url == "/"


@pytest.mark.django_db
def test_register(client):
    reg = client.get("/index/")
    assert reg.context["name"] == 1
