import datetime

from django.db.models import Avg, Count, F, Q

from books.models import Author, Book, Review


def find_authors_by_name(name: str):
    """Найди всех авторов с именем «John»."""
    return Author.objects.filter(first_name=name)


def find_authors_exclude_last_name(last_name: str):
    """Найди всех авторов, кроме тех, у кого фамилия «Doe»."""
    return Author.objects.exclude(last_name=last_name)


def find_books_price_less_than(price: int):
    """Найди все книги, цена которых меньше 500."""
    return Book.objects.filter(price__lt=price)


def find_books_price_lte(price: int):
    """Найди все книги с ценой не более 300."""
    return Book.objects.filter(price__lte=price)


def find_books_price_greater_than(price: int):
    """Найди все книги дороже 1000."""
    return Book.objects.filter(price__gt=price)


def find_books_price_gte(price: int):
    """Найди все книги с ценой от 750 и выше."""
    return Book.objects.filter(price__gte=price)


def find_books_with_word_in_title(word: str):
    """Найди все книги, содержащие слово «django» в названии."""
    return Book.objects.filter(title__icontains=word)


def find_books_title_starts_with(prefix: str):
    """Найди книги, название которых начинается со слова «Advanced»."""
    return Book.objects.filter(title__startswith=prefix)


def find_books_title_starts_with_case_insensitive(prefix: str):
    """Найди книги, название которых начинается с «pro» (игнорируя регистр)."""
    return Book.objects.filter(title__istartswith=prefix)


def find_books_title_ends_with(suffix: str):
    """Найди книги, название которых заканчивается на слово «Guide»."""
    return Book.objects.filter(title__endswith=suffix)


def find_books_title_ends_with_case_insensitive(suffix: str):
    """Найди книги, название которых заканчивается на «tutorial» (без учёта регистра)."""
    return Book.objects.filter(title__iendswith=suffix)


def find_reviews_with_no_comment():
    """Найди все отзывы без комментариев."""
    return Review.objects.filter(comment__isnull=True)


def find_reviews_with_comment():
    """Найди все отзывы, у которых есть комментарий."""
    return Review.objects.filter(comment__isnull=False)


def find_authors_by_ids(ids: list[int]):
    """Найди авторов с идентификаторами 1, 3 и 5."""
    return Author.objects.filter(id__in=ids)


def find_books_published_in_date_range(
    start_date: datetime.date, end_date: datetime.date
):
    """Найди книги, опубликованные с 1 января по 31 декабря 2023 года."""
    return Book.objects.filter(published_date__range=(start_date, end_date))


def find_authors_last_name_starts_with_case_insensitive(prefix: str):
    """Найди авторов, чья фамилия начинается на «Mc» (игнорируя регистр)."""
    return Author.objects.filter(last_name__istartswith=prefix)


def find_books_published_in_year(year: int):
    """Найди книги, опубликованные в 2024 году."""
    return Book.objects.filter(published_date__year=year)


def find_books_published_in_month(month: int):
    """Найди книги, опубликованные в июне."""
    return Book.objects.filter(published_date__month=month)


def find_reviews_on_day_of_month(day: int):
    """Найди отзывы, оставленные 11-го числа любого месяца."""
    return Review.objects.filter(created_at__day=day)


def find_books_published_in_week_of_year(week: int):
    """Найди книги, опубликованные на 23-й неделе года."""
    return Book.objects.filter(published_date__week=week)


def find_reviews_on_iso_weekday(weekday: int):
    """Найди отзывы, оставленные во вторник."""
    return Review.objects.filter(created_at__iso_week_day=weekday)


def find_books_published_in_quarter(quarter: int):
    """Найди книги, опубликованные во втором квартале года."""
    return Book.objects.filter(published_date__quarter=quarter)


def find_reviews_on_date(date: datetime.date):
    """Найди отзывы, сделанные в определённую дату."""
    return Review.objects.filter(created_at__date=date)


def find_reviews_at_time(time: datetime.time):
    """Найди отзывы, сделанные ровно в 15:30."""
    return Review.objects.filter(created_at__time=time)


def find_reviews_at_hour(hour: int):
    """Найди отзывы, сделанные в 15 часов."""
    return Review.objects.filter(created_at__hour=hour)


def find_reviews_at_minute(minute: int):
    """Найди отзывы, сделанные в 30 минут любого часа."""
    return Review.objects.filter(created_at__minute=minute)


def find_reviews_at_second(second: int):
    """Найди отзывы, созданные в момент, когда секунды были равны 0."""
    return Review.objects.filter(created_at__second=second)


def find_books_by_author_email(email: str):
    """Найди книги, написанные автором с почтой «author@example.com»."""
    return Book.objects.filter(author__email=email)


def find_books_by_author_last_name_contains(name_part: str):
    """Найди книги авторов, чья фамилия содержит «smith» (без учёта регистра)."""
    return Book.objects.select_related("author").filter(
        author__last_name__icontains=name_part
    )


def find_authors_with_more_than_n_books(n: int):
    """Найди авторов, написавших более пяти книг."""
    return Author.objects.annotate(book_count=Count("books")).filter(book_count__gt=n)


def find_books_with_metadata_genre(genre: str):
    """Найди книги, у которых значение ключа «genre» равно «fiction»."""
    return Book.objects.filter(metadata__genre=genre)


def find_books_with_metadata_tag(tag: str):
    """Найди книги, где значение ключа «tags» содержит слово «bestseller»."""
    return Book.objects.filter(metadata__tags__icontains=tag)


def find_books_with_price_equal_to_discount():
    """Найди книги, у которых цена равна скидке."""
    return Book.objects.filter(price=F("discount"))


def find_books_with_price_greater_than_discount():
    """Найди книги, у которых цена больше скидки."""
    return Book.objects.filter(price__gt=F("discount"))


def find_authors_by_name_or_not_last_name(name: str, last_name: str):
    """Найди авторов с именем «Alice» или с фамилией, не равной «Brown»."""
    return Author.objects.filter(Q(first_name=name) | ~Q(last_name=last_name))


def count_books_by_each_author():
    """Подсчитай количество книг каждого автора."""
    return Author.objects.annotate(books_amount=Count("books"))


def get_average_rating_for_each_book():
    """Подсчитай средний рейтинг каждой книги."""
    return Book.objects.annotate(avg_rating=Avg("reviews__rating"))


def get_books_with_actual_price():
    """Посчитай окончательную цену книги (цена минус скидка)."""
    return Book.objects.annotate(actual_price=F("price") - F("discount"))


def get_books_with_authors():
    """Получи список книг и авторов так, чтобы выполнить всего один SQL-запрос."""
    return Book.objects.select_related("author")


def get_authors_with_their_books():
    """Получи список авторов и всех их книг так, чтобы было выполнено ровно два SQL-запроса."""
    return Author.objects.prefetch_related("books")
