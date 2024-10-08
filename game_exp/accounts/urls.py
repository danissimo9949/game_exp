from django.urls import path
from .views import UserCreate, UserDetail, UserProfileUpdate, UserProfile, EmailNotification
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-create', UserCreate.as_view(), name='user-create'),
    path('user-detail', UserDetail.as_view()),

    path('profile', UserProfileUpdate.as_view(), name='user-profile-update'),
    path('profile/<str:username>', UserProfile.as_view(), name='user-profile'),
    path('profile/settings/email-notification', EmailNotification.as_view())
]