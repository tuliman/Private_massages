from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse

from .models import Chats, Messages,Comment,Profile,News
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationUserForm, AuthUserForm, MessagesForm


# Create your views here.
def auth(request):
    if request.method == 'POST':
        form = AuthUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['user_name'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                HttpResponse('Disabled')

    else:
        form = AuthUserForm()
        return render(request, 'chat/login.html', {'form': form})


class LogoutProfile(LogoutView):
    template_name = 'chat/logout.html'


def registration(request):
    if request.method == 'POST':
        form = RegistrationUserForm(request.POST)
        if form.is_valid():

            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Baned_User.objects.create(user=new_user)

            return redirect('auth')
        else:
            return render(request, 'chat/register.html', {'form': form})
    else:
        form = RegistrationUserForm()
        context = {
            'form': form
        }
        return render(request, 'chat/register.html', context)


def profile(request, ):
    user = request.user
    search_q = request.GET.get('q')
    search_users = ''
    obj = User.objects.filter(username=user)
    if search_q is not None:
        search_users = User.objects.filter(username__exact=search_q)

        print(len(search_users))
        if len(search_users) > 0:
            search_users = search_users
        else:
            pass

    context = {'obj': obj, 'user': user, 'search_users': search_users}
    return render(request, 'chat/profile.html', context, )


def anny_user_profile(request, id):
    user = request.user
    opponent_profile = get_object_or_404(User, id=id)
    return render(request, 'chat/anny_user_profile.html', {'opponent': opponent_profile, 'user': user})


def create_chat(request, opponent_id):
    user = request.user
    opponent_id = get_object_or_404(User, id=opponent_id)

    chat = Chats.objects.filter(user_1=user, opponent=opponent_id)
    op = Chats.objects.filter(user_1=opponent_id, opponent=user)
    if chat.count() > 0 or op.count() > 0:
        if op:
            chat = op
        else:
            chat = chat
    if chat.count() == 0:
        chat = Chats.objects.create(user_1=user, opponent=opponent_id)
    else:
        chat = chat.first()

    return redirect(reverse('dialog', kwargs={'chat_id': chat.id}))


class ChatMessages(View):
    def get(self, request, chat_id):
        user = request.user
        form = MessagesForm()

        message = Messages.objects.filter(chat_id=chat_id)

        return render(request, 'chat/dialog.html', {'form': form, 'message': message})

    def post(self, request, chat_id):
        form = MessagesForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            chat_id = Chats.objects.get(id=chat_id)

            message.chat_id = chat_id
            message.author = request.user
            message.save()

            return redirect(reverse('dialog', kwargs={'chat_id': chat_id.id}))
