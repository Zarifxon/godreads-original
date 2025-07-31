from django.test import TestCase
from django.urls import reverse


from books.models import Book, BookReview
from users.models import CustomUser


# Create your tests here.



class BooksTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse("books:list"))

        self.assertContains(response, "No books found")

    def test_books_list(self):
        book1=Book.objects.create(title="Book1", description="descrip1", isbn="11111111")
        book2=Book.objects.create(title="Book2", description="descrip2", isbn="22222222")
        book3=Book.objects.create(title="Book3", description="descrip3", isbn="33333333")


        response = self.client.get(reverse("books:list") +"?page_size=2")


        for book in [book1, book2]:
            self.assertContains(response, book.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse("books:list") +"?page=2&?page_size=2")
        self.assertContains(response, book3.title)



    def test_detail_page(self):
        book = Book.objects.create(title="Book1", description="descrip1", isbn="11111111")

        response = self.client.get(reverse("books:detail", kwargs={"id": book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)


    def test_search_books(self):
        book1 = Book.objects.create(title="Sport", description="descrip1", isbn="11111111")
        book2 = Book.objects.create(title="Mening birinchi ishim", description="descrip2", isbn="22222222")
        book3 = Book.objects.create(title="Sen qayerdasan", description="descrip3", isbn="33333333")

        response = self.client.get(reverse("books:list")+ "?q=Sport")
        self.assertContains(response, book1.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse("books:list") + "?q=Mening birinchi ishim")
        self.assertContains(response, book2.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse("books:list") + "?q=Sen qayerdasan")
        self.assertContains(response, book3.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book2.title)


class BookReviewTestCase(TestCase):
    def test_add_review(self):
        book = Book.objects.create(title='Book', description='Description test')
        user = CustomUser.objects.create(
            username="zarif", first_name="zarif", last_name="isoxonov", email="zarifsf@mail.ru"
        )
        user.set_password("somepass")
        user.save()

        self.client.login(username="zarif", password="somepass")

        self.client.post(reverse('books:reviews', kwargs={"id":book.id}), data={
            "stars_given": 3,
            "comment": "Nice book"
        })
        book_reviews = book.bookreview_set.all()

        self.assertEqual(book_reviews.count(), 1)
        self.assertEqual(book_reviews[0].stars_given, 3)
        self.assertEqual(book_reviews[0].comment, "Nice book")
        self.assertEqual(book_reviews[0].book, book)
        self.assertEqual(book_reviews[0].user, user)

    