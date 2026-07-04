import pytest

from src.article import Article

# ==========================
# Запуск тестов в модуле
# pytest tests/test_search.py
# ==========================

@pytest.fixture
def list_articles():
    Article.articles = dict()
    Article.insert('test1', 'test1')
    Article.insert('test2', 'test2')
    Article.insert('test3', 'test3')
    Article.insert('test4', 'test4')
    Article.insert('test5', 'test5')


def test_search_3(list_articles):
    """ Проверяем поиск статьи по ID """
    searchable_article = Article.search(3)
    assert searchable_article.title == 'test3'


def test_search_4(list_articles):
    """ Проверяем поиск статьи по ID """
    searchable_article = Article.search(4)
    assert searchable_article.title == 'test4'