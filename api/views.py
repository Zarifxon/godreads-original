from django.core.serializers import serialize
from django.http import JsonResponse
from django.views import View
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from books.models import BookReview
from api.serializers import BookReviewSerializer


# BU pastdagi classlar ko'p ishltilganligi sababli kodni kichraytirish maqsadida viewsetlardan foydalaniladi'
class BookReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookReviewSerializer
    queryset = BookReview.objects.all().order_by('-created_at')
    lookup_field = "id"


# o'zimiz yozishimiz uchun Django view ishlatsak '
# restda esa APIViewni ishlatamiz


# Bir qancha kodlarni generic viewda yozilganligi sababli bu kodlarni qayta yozish shart emas
# Quyidagicha qilib yozsa bo'ladi

# class BookReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = BookReviewSerializer
#     queryset = BookReview.objects.all()
#     lookup_field = "id"
#
# # class BookReviewDetailAPIView(APIView):
# #     permission_classes = [IsAuthenticated]
#
# #     def get(self, request, id):
# #         book_review = BookReview.objects.get(id=id)
# #
# #         # json_response = {
# #         #     "id": book_review.id,
# #         #     "stars_given": book_review.stars_given,
# #         #     "comment":book_review.comment,
# #         #     "book": {
# #         #         "id": book_review.book.id,
# #         #         "title": book_review.book.title,
# #         #         "description": book_review.book.description,
# #         #         "isbn": book_review.book.isbn,
# #         #     },
# #         #     "users": {
# #         #         "id": book_review.user.id,
# #         #         "first_name":book_review.user.first_name,
# #         #         "last_name": book_review.user.last_name,
# #         #         "username": book_review.user.username
# #         #     }
# #         # }
# #         serializer = BookReviewSerializer(book_review)
# #
# #         # return JsonResponse(json_response)
# #         return Response(data=serializer.data)
# #
# #     def delete(self, request, id):
# #         book_review = BookReview.objects.get(id=id)
# #         book_review.delete()
# #
# #         return Response(status=status.HTTP_204_NO_CONTENT)
# #
# #     def put(self, request, id):
# #         book_review = BookReview.objects.get(id=id)
# #         serializer = BookReviewSerializer(instance=book_review, data=request.data)
# #
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(data=serializer.data, status=status.HTTP_200_OK)
# #         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
# # # reviewni o'zgartirishda faqat bir elementni o'zgartirmoqchi bo'lsak patchdan foydalanamiz
# #     def patch(self, request, id):
# #         book_review = BookReview.objects.get(id=id)
# #         serializer = BookReviewSerializer(instance=book_review, data=request.data, partial=True)
# #
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(data=serializer.data, status=status.HTTP_200_OK)
# #         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class BookReviewsAPIView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = BookReviewSerializer
#     queryset = BookReview.objects.all().order_by('-created_at')
#
# #
# # class BookReviewsAPIView(APIView):
# #     permission_classes = [IsAuthenticated]
# #
# #     def get(self, request):
# #         book_reviews = BookReview.objects.all().order_by('-created_at')
# #
# #         paginator = PageNumberPagination()
# #         page_obj = paginator.paginate_queryset(book_reviews, request)
# #
# #         serializer = BookReviewSerializer(page_obj, many=True)
# #         return paginator.get_paginated_response(serializer.data)
# #
# #     def post(self, request):
# #         serializer = BookReviewSerializer(data=request.data)
# #
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
# #
# #         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
