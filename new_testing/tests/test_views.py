import pytest
from mixer.backend.django import mixer
from django.test import RequestFactory
from posts import views


pytestmark = pytest.mark.django_db


class TestPostsViews:

    def test_show_post(self):
        post = mixer.blend('posts.BlogPost', text='lists of tests')
        req = RequestFactory().get('/')
        resp = views.show_post(req)
        assert 'lists of tests'
        assert resp.status_code == 200, 'should be callable by anyone'
