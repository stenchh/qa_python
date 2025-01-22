from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_dublicate(self):
        collector = BooksCollector()

        collector.add_new_book('Как разговаривать')
        collector.add_new_book('Как разговаривать')

        assert len(collector.books_genre) == 1

    def test_add_new_book_add_book_len_39_added(self):
        collector = BooksCollector()

        collector.add_new_book('Сказка о Тройке. История непримиримой б')

        assert len(collector.books_genre) == 1

    def test_add_new_book_add_book_len_40_added(self):
        collector = BooksCollector()

        collector.add_new_book('Сказка о Тройке. История непримиримой бо')

        assert len(collector.books_genre) == 1

    def test_add_new_book_add_book_len_6_added(self):
        collector = BooksCollector()

        collector.add_new_book('Сказка')

        assert len(collector.books_genre) == 1

    def test_add_new_book_add_book_len_1_added(self):
        collector = BooksCollector()

        collector.add_new_book('С')

        assert len(collector.books_genre) == 1

    def test_add_new_book_add_book_len_41_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('Сказка о Тройке. История непримиримой бор')

        assert len(collector.books_genre) == 0

    def test_add_new_book_add_book_len_42_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('Сказка о Тройке. История непримиримой борь')

        assert len(collector.books_genre) == 0

    def test_add_new_book_add_book_len_zero_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('')

        assert len(collector.books_genre) == 0

    def test_add_new_book_add_book_len_262_not_added(self):
        collector = BooksCollector()

        collector.add_new_book(
            'Сказка о Тройке. История непримиримой борьбы за повышение трудовой дисциплины, против бюрократизма, за высокий моральный уровень, против обезлички, за здоровую критику и здоровую самокритику, за личную ответственность каждого, за образцовое содержание отчетности и против недооценки собственных сил')

        assert len(collector.books_genre) == 0

    def test_set_book_genre_genre_in_books_genre(self):
        collector = BooksCollector()
        book_title = 'Сказка'
        genre = 'Мультфильмы'

        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, genre)

        assert collector.books_genre[book_title] == genre

    def test_set_book_genre_genre_not_in_books_genre(self):
        collector = BooksCollector()
        book_title = 'Как разговаривать'
        invalid_genre = 'Психология'

        collector.add_new_book(book_title)

        collector.set_book_genre(book_title, invalid_genre)

        assert collector.get_book_genre(book_title) == ''

    def test_get_book_genre_in_books_genre(self):
        collector = BooksCollector()
        book_title = 'Война миров'
        book_genre = 'Фантастика'

        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, book_genre)

        assert collector.get_book_genre(book_title) == book_genre

    def test_get_book_genre_not_in_books_genre(self):
        collector = BooksCollector()
        book_title = 'Как разговаривать'
        invalid_genre = 'Психология'

        collector.add_new_book(book_title)

        collector.set_book_genre(book_title, invalid_genre)

        assert collector.get_book_genre(book_title) == ''

    def test_get_books_with_specific_genre_list_of_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')

        collector.add_new_book('Сумерки')
        collector.set_book_genre('Сумерки', 'Ужасы')

        result = collector.get_books_with_specific_genre('Ужасы')
        expected = ['Дракула', 'Сумерки']

        assert result == expected

    def test_get_books_with_specific_genre_empty_list(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')

        result = collector.get_books_with_specific_genre('Детективы')
        assert result == []

        result_invalid_genre = collector.get_books_with_specific_genre('Научпоп')
        assert result_invalid_genre == []

    def test_get_books_genre_empty(self):
        collector = BooksCollector()

        result = collector.get_books_genre()
        assert result == {}

    def test_get_books_genre_list_of_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')

        expected_books_genre = {
            'Гарри Поттер': 'Фантастика',
            'Дракула': 'Ужасы'
        }

        result = collector.get_books_genre()

        assert result == expected_books_genre

    def test_get_books_for_children_list_of_books(self):
        collector = BooksCollector()

        collector.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        collector.genre_age_rating = ['Ужасы', 'Детективы']

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')

        collector.add_new_book('Том и Джерри')
        collector.set_book_genre('Том и Джерри', 'Мультфильмы')

        expected_books_for_children = ['Гарри Поттер', 'Том и Джерри']

        result = collector.get_books_for_children()

        assert result == expected_books_for_children

    def test_get_books_for_children_empty(self):
        collector = BooksCollector()

        collector.genre = ['Фантастика', 'Ужасы', 'Детективы']
        collector.genre_age_rating = ['Ужасы', 'Детективы']

        result = collector.get_books_for_children()

        assert result == []

    def test_get_books_for_children_genres_with_age_restrictions(self):
        collector = BooksCollector()

        collector.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        collector.genre_age_rating = ['Ужасы', 'Детективы']

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')

        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        collector.add_new_book('Неизвестная книга')
        collector.set_book_genre('Неизвестная книга',
                                 'Непонятный жанр')

        result = collector.get_books_for_children()

        assert 'Дракула' not in result
        assert 'Шерлок Холмс' not in result
        assert 'Неизвестная книга' not in result

    def test_add_book_in_favorites_positive(self):
        collector = BooksCollector()

        book_title = 'Гарри Поттер'
        book_genre = 'Фантастика'

        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, book_genre)
        collector.add_book_in_favorites(book_title)

        assert book_title in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_book_not_in_books_genre(self):
        collector = BooksCollector()
        book_title = 'Гарри Поттер'
        collector.add_book_in_favorites(book_title)

        assert book_title not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_book_already_in_favorites(self):
        collector = BooksCollector()

        book_title = 'Гарри Поттер'

        collector.add_new_book(book_title)
        collector.add_book_in_favorites(book_title)

        collector.add_book_in_favorites(book_title)

        assert collector.get_list_of_favorites_books().count(book_title) == 1

    def test_delete_book_from_favorites_deleted(self):
        collector = BooksCollector()

        book_title = 'Гарри Поттер'
        collector.add_new_book(book_title)
        collector.add_book_in_favorites(book_title)

        collector.delete_book_from_favorites(book_title)

        assert book_title not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_not_in_favorites(self):
        collector = BooksCollector()

        book_title = 'Гарри Поттер'
        collector.add_book_in_favorites('Волшебник из страны Оз')

        collector.delete_book_from_favorites(book_title)

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_empty_favorites(self):
        collector = BooksCollector()
        book_title = 'Гарри Поттер'

        collector.delete_book_from_favorites(book_title)

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_books_in_the_list(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Властелин колец')

        result = collector.get_list_of_favorites_books()

        assert 'Гарри Поттер' in result
        assert 'Властелин колец' in result

    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()

        result = collector.get_list_of_favorites_books()

        assert result == []





