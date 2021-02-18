from django.urls import path

from .views import profile, registration, auth, anny_user_profile, create_chat, ChatMessages, LogoutProfile, view_news, \
    AddNews

urlpatterns = [
    path('auth/', auth, name='auth'),
    path('logout/', LogoutProfile.as_view(), name='logout'),
    path('register/', registration, name='registration'),
    path('', profile, name='profile'),
    path('profile/<int:id>/', anny_user_profile, name='any_user_id'),
    path('<int:opponent_id>/dialog/', create_chat, name='create_chat'),
    path('dialog/<int:chat_id>/', ChatMessages.as_view(), name='dialog'),
    path('news/', view_news, name='news'),
    path('news/create/', AddNews.as_view(), name='create')

]
