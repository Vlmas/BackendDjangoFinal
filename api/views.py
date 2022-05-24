import http
import json
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, BasePermission, SAFE_METHODS
from api.models import *
from api.serializers import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            (request.user and request.user.is_staff)
        )


permission_classes = (IsAdminUser, IsAuthenticated, IsAdminOrReadOnly)


class BookViewSet(viewsets.ViewSet):
    permission_classes = (IsAdminUser, IsAuthenticated, IsAdminOrReadOnly)

    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        data = serializer.data

        return Response(data, status=http.HTTPStatus.OK)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book)
        data = serializer.data

        return Response(data, status=http.HTTPStatus.OK)


class JournalViewSet(viewsets.ViewSet):
    permission_classes = (IsAdminUser, IsAuthenticated, IsAdminOrReadOnly)

    def list(self, request):
        queryset = Journal.objects.all()
        serializer = JournalSerializer(queryset, many=True)
        data = serializer.data

        return Response(data, status=http.HTTPStatus.OK)

    def retrieve(self, request, pk=None):
        queryset = Journal.objects.all()
        journal = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(journal)
        data = serializer.data

        return Response(data, status=http.HTTPStatus.OK)


class BookListAPIView(APIView):
    permission_classes = (IsAdminUser, IsAuthenticated, IsAdminOrReadOnly)

    def get(self, request):
        books = Book.objects.all()
        ser = BookSerializer(books, many=True)
        data = ser.data

        return Response(data, status=http.HTTPStatus.OK)

    def post(self, request):
        ser = BookSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            data = ser.data
            return Response(data, http.HTTPStatus.CREATED)

        return Response(ser.errors, status=http.HTTPStatus.BAD_REQUEST)


class BookDetailsAPIView(APIView):
    permission_classes = (IsAdminUser, IsAuthenticated, IsAdminOrReadOnly)

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise http.HTTPStatus.NOT_FOUND

    def get(self, request, pk):
        book = self.get_object(pk)
        ser = BookSerializer(book)
        data = ser.data

        return Response(data, status=http.HTTPStatus.OK)

    def put(self, request, pk):
        book = self.get_object(pk)
        ser = BookSerializer(instance=book, data=request.data)

        if ser.is_valid():
            ser.save()
            data = ser.data
            return Response(data, http.HTTPStatus.ACCEPTED)

        return Response(ser.errors, http.HTTPStatus.BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response({
            'message': 'book deleted'
        }, status=http.HTTPStatus.OK)


class JournalListAPIView(APIView):
    permission_classes = (IsAdminUser, IsAuthenticated, IsAdminOrReadOnly)

    def get(self, request):
        journals = Journal.objects.all()
        ser = JournalSerializer(journals, many=True)
        data = ser.data

        return Response(data, status=http.HTTPStatus.OK)

    def post(self, request):
        ser = JournalSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            data = ser.data
            return Response(data, http.HTTPStatus.CREATED)

        return Response(ser.errors, http.HTTPStatus.BAD_REQUEST)


class JournalDetailsAPIView(APIView):
    permission_classes = (IsAdminUser, IsAuthenticated, IsAdminOrReadOnly)

    def get_object(self, pk):
        try:
            return Journal.objects.get(pk=pk)
        except Journal.DoesNotExist:
            raise http.HTTPStatus.NOT_FOUND

    def get(self, request, pk):
        journal = self.get_object(pk)
        ser = BookSerializer(journal)
        data = ser.data

        return Response(data, status=http.HTTPStatus.OK)

    def put(self, request, pk):
        journal = self.get_object(pk)
        ser = JournalSerializer(instance=journal, data=request.data)

        if ser.is_valid():
            ser.save()
            data = ser.data
            return Response(data, http.HTTPStatus.ACCEPTED)

        return Response(ser.errors, http.HTTPStatus.BAD_REQUEST)

    def delete(self, request, pk):
        journal = self.get_object(pk)
        journal.delete()
        return Response({
            'message': 'journal deleted'
        }, status=http.HTTPStatus.OK)


class CreateUserAPIView(APIView):
    permission_classes = (IsAdminUser, IsAuthenticated, IsAdminOrReadOnly)

    def post(self, request):
        print(request.data)
        data = request.data
        user = User.objects.create_user(username=data['username'], password=data['password'], email=data['email'])
        user.save()

        return Response(data, status=http.HTTPStatus.CREATED)

