import pytest
from mixer.backend.django import mixer
from .fixture import (full_text, wanted)


pytestmark = pytest.mark.django_db


class TestPost:
    def test_init(self):
        obj = mixer.blend('posts.BlogPost')
        assert obj.pk == 1, 'Should save an instance'

    def test_get_excerpt(self):
        obj = mixer.blend('posts.BlogPost', text=full_text)
        result = obj.get_excerpt()
        expected = wanted
        assert result == expected, 'should be 3 lines'

    def test_author(self):
        obj = mixer.blend('posts.BlogPost', author=None)

        result = obj.author
        expected = 'Anon'
        assert result == expected, 'Should be Anon'
