from django.urls import path

from .views import profile, registration, auth, anny_user_profile, create_chat, ChatMessages, LogoutProfile, ViewNews, \
    AddNews,chat_list

urlpatterns = [
    path('auth/', auth, name='auth'),
    path('logout/', LogoutProfile.as_view(), name='logout'),
    path('register/', registration, name='registration'),
    path('', profile, name='profile'),
    path('profile/<int:id>/', anny_user_profile, name='any_user_id'),
    path('<int:opponent_id>/dialog/', create_chat, name='create_chat'),
    path('dialig/dialoglist/',chat_list,name='dialog_list'),
    path('dialog/<int:chat_id>/', ChatMessages.as_view(), name='dialog'),
    path('news/', ViewNews.as_view(), name='news'),
    path('news/create/', AddNews.as_view(), name='create')

]
