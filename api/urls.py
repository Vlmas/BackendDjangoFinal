from django.urls import path, include
from rest_framework import routers
from api.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register('book-viewset', BookViewSet, basename='Book')
router.register('journal-viewset', JournalViewSet, basename='Journal')

urlpatterns = [
    path('/', include(router.urls)),

    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token-verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/sign-up/', CreateUserAPIView.as_view()),

    path('books/', BookListAPIView.as_view()),
    path('books/<int:pk>/', BookDetailsAPIView.as_view()),

    path('journals/', JournalListAPIView.as_view()),
    path('journals/<int:pk>/', JournalDetailsAPIView.as_view()),
]
