from django.urls import path
from .views import UserCreate, UserList

urlpatterns = [
    path('user-create', UserCreate.as_view(), name='user-create'),
    path('users-all', UserList.as_view())
]