from django.test import TestCase
from django.urls import reverse

from books.models import Book, BookReview
from users.models import CustomUser


class HomePageTestCase(TestCase):
    def test_paginated_list(self):
        book = Book.objects.create(title="Book1", description="descrip1", isbn="11111111")
        user = CustomUser.objects.create(
            username="zarif", first_name="zarif", last_name="isoxonov", email="zarifsf@mail.ru"
        )
        user.set_password("somepass")
        user.save()

        review1=BookReview.objects.create(book=book, user=user, stars_given=3, comment="very good book")
        review2=BookReview.objects.create(book=book, user=user, stars_given=4, comment="very emas good book")
        review3=BookReview.objects.create(book=book, user=user, stars_given=5, comment="very borib kel good book")

        response = self.client.get(reverse("home_page") +"?page_size=2")
        self.assertContains(response, review3.comment)
        self.assertContains(response, review2.comment)
        self.assertNotContains(response, review1.comment)


