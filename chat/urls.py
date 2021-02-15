from django.urls import path
from django.contrib.auth.views import auth_logout
from .views import profile, registration, auth, anny_user_profile, create_chat,ChatMessages

urlpatterns = [
    path('auth/', auth, name='auth'),
    path('logout/', auth_logout, name='logout'),
    path('register/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('profile/<int:id>/', anny_user_profile, name='any_user_id'),
    path('<int:opponent_id>/dialog/', create_chat, name='create_chat'),
    path('/dialog/<int:chat_id>/',ChatMessages.as_view(),name='dialog')

]
