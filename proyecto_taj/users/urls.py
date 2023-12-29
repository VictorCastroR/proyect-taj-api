from django.urls import path
from .views import UserList, UserDetail, UserRegistration

urlpatterns = [
    path('list/', UserList.as_view(), name='user-list'),
    path('detail/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('users/register/', UserRegistration.as_view(), name='user-registration'),
    # Agrega otras rutas según sea necesario
]
