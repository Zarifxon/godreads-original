from rest_framework import serializers

from books.models import Book, BookReview
from users.models import CustomUser


# Biz bu serializerlarni soddalashtirish uchun modelSerializerdan foydalanamiz

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "description", "isbn")

# class BookSerializer(serializers.Serializer):
    # title = serializers.CharField(max_length=200)
    # description = serializers.CharField()
    # isbn = serializers.CharField(max_length=17)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name", "email", "username")



#
# class UserSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=200)
#     last_name = serializers.CharField(max_length=200)
#     username = serializers.CharField(max_length=200)
#     email = serializers.CharField(max_length=255)




class BookReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    book_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = BookReview
        fields = ("id", "stars_given", "comment", "book", "user", "user_id", "book_id")

# class BookReviewSerializer(serializers.Serializer):
#     stars_given = serializers.IntegerField(min_value=1, max_value=5)
#     comment = serializers.CharField()
#     book = BookSerializer()
#     user = UserSerializer()
