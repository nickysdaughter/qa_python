import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_one_book(self, collector):
        collector.add_new_book('Test book')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('book_name', ['', 'BookWithAVeryLongNameThatExceedsFortyCharacters'])
    def test_add_new_book_more_40_or_zero_name_chars(self, collector, book_name):
        collector.add_new_book(book_name)
        assert collector.books_genre == {}

    def test_set_book_genre_new_genre(self, collector):
        collector.add_new_book('First test book')
        collector.set_book_genre('First test book', 'Ужасы')
        assert collector.books_genre['First test book'] == 'Ужасы'

    def test_set_book_genre_non_existent_genre(self, collector):
        collector.add_new_book('Another book')
        collector.set_book_genre('Another book', 'Blah-blah-genre')
        assert collector.books_genre['Another book'] == ''

    def test_get_book_genre_existing_genre(self, collector):
        collector.add_new_book('I dont wanna do it book')
        collector.set_book_genre('I dont wanna do it book', 'Фантастика')
        assert collector.books_genre['I dont wanna do it book'] == 'Фантастика'

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('First Detective book')
        collector.add_new_book('Second Detective book')
        collector.add_new_book('Cartoon book')
        collector.set_book_genre('First Detective book', 'Детективы')
        collector.set_book_genre('Second Detective book', 'Детективы')
        collector.set_book_genre('Cartoon book', 'Мультфильмы')
        detective_books = collector.get_books_with_specific_genre('Детективы')
        assert len(detective_books) == 2

    def test_get_books_genre_two_books(self, collector):
        collector.add_new_book('Help me book')
        collector.add_new_book('SOS book')
        collector.set_book_genre('Help me book', 'Комедии')
        collector.set_book_genre('SOS book', 'Ужасы')
        assert len(collector.get_books_genre()) == 2

    def test_get_books_for_children_one_book(self, collector):
        collector.add_new_book('Fantastic book')
        collector.set_book_genre('Fantastic book', 'Фантастика')
        collector.add_new_book('Horror book')
        collector.set_book_genre('Book2', 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert len(books_for_children) == 1

    def test_add_book_in_favorites_new_book(self, collector):
        collector.add_new_book('Favorite book')
        collector.add_book_in_favorites('Favorite book')
        assert collector.favorites == ['Favorite book']

    def test_add_book_in_favorites_already_added_book(self, collector):
        collector.add_new_book('Favorite book')
        collector.add_book_in_favorites('Favorite book')
        collector.add_book_in_favorites('Favorite book')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_empty_list(self, collector):
        collector.add_new_book('Favorite book')
        collector.add_book_in_favorites('Not so favorite book')
        collector.delete_book_from_favorites('Not so favorite book')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_one_book(self, collector):
        collector.add_new_book('Favorite book')
        collector.add_new_book('Not favorite book')
        collector.add_book_in_favorites('Favorite book')
        assert collector.favorites == ['Favorite book']

