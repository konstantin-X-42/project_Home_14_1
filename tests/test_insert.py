import pytest

from src.article import Article

# ==========================
# Запуск тестов в модуле
# pytest tests/test_insert.py
# ==========================

@pytest.fixture
def one_article():
    Article.articles = dict() # обнуляем словарь перед каждым тестом
    return Article.insert('test', 'test')


@pytest.fixture
def two_articles():
    Article.articles = dict() # удаляем статьи перед каждым тестом
    Article.insert('test', 'test')
    return Article.insert('test', 'test')


def test_insert(one_article):
    """ Проверяем, что количество статей ровно единице """
    assert len(Article.articles) == 1


def test_article_id(one_article):
    """ Проверка установки ID статьи """
    assert one_article.article_id == 1


def test_increase_id(two_articles):
    """ Проверяем увеличение ID статьи"""
    assert two_articles.article_id == 2


def test_increase_articles_count(two_articles):
    """ Проверяем увеличение списка статей """
    assert len(Article.articles) == 2
