from django.contrib.auth import login
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Friendship
from django.db.models import Q
import datetime
import requests
import json

token = "161aeba8-e0d8-4e28-982d-7f0e042f83ca"


def index(request):
    context = {}
    context['users'] = reversed(
        User.objects.all().order_by('-date_created')[:5])
    return render(request, 'facethemapp/index.html', context=context)


def developer(request):
    context = {}
    if request.session.get('user', False):
        return render(request, 'facethemapp/developer.html')
    else:
        context['error'] = "You have to sign in :)"
        return render(request, 'facethemapp/error.html', context=context)


def friends(request):
    context = {}
    if request.session.get('user', False):
        return render(request, 'facethemapp/friends.html')
    else:
        context['error'] = "You have to sign in :)"
        return render(request, 'facethemapp/error.html', context=context)


def friends_profile(request, username):
    context = {}
    friends = []
    user = User.objects.filter(username=username).first()
    print(user)
    friendships = Friendship.objects.filter(
        Q(person_1=user.player_id) | Q(person_2=user.player_id))
    print(friendships)
    for item in friendships:
        if item.person_1 == user:
            print("Ubacujem drugog igraca %s" % item.person_2.username)
            friends.append(item.person_2)
        else:
            print("Ubacujem pvrog igraca %s" % item.person_1.username)
            friends.append(item.person_1)
    print(friends)
    context['friends'] = friends
    return render(request, 'facethemapp/friends-profile.html', context=context)


def latest_matches(request):
    context = {}
    context['error'] = 'This page is not yet implemented'
    return render(request, 'facethemapp/error.html', context=context)


def logout_user(request):
    try:
        del request.session['user']
        del request.session['username']
        del request.session['elo']
        del request.session['cover']
        del request.session['avatar']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('index'))


def login_user(request):
    context = {}
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email, password=password).first()
        if user is not None:
            url = f"https://open.faceit.com/data/v4/players?nickname={user.username}"
            response = requests.get(
                url, headers={"Authorization": 'Bearer {}'.format(token)})
            obj = json.loads(response.text)
            elo = obj['games']['csgo']['faceit_elo']
            print(elo)
            request.session['user'] = True
            request.session['username'] = user.username
            request.session['elo'] = elo
            request.session['cover'] = user.cover_image
            request.session['avatar'] = user.avatar
            return render(request, 'facethemapp/profile.html')
        else:
            context['error'] = "Please, check your credentials!"
            return render(request, 'facethemapp/login.html', context=context)
    else:
        return render(request, 'facethemapp/login.html')


def profile(request, username):
    context = {}
    if username == 'default':
        context['error'] = 'You are not logged in!'
        return render(request, 'facethemapp/error.html', context=context)
    context['username'] = username
    return render(request, 'facethemapp/profile.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['nickname']
        date = request.POST['date']
        user = User.objects.filter(username=username).first()
        if user is not None:
            return HttpResponseRedirect(reverse('login'))
        url = f"https://open.faceit.com/data/v4/players?nickname={username}"
        response = requests.get(
            url, headers={"Authorization": 'Bearer {}'.format(token)})
        obj = json.loads(response.text)
        user = User(player_id=obj['player_id'], username=username, email=email, password=password, date=date,
                    avatar=obj['avatar'], cover_image=obj['cover_image'])
        user.save()
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'facethemapp/register.html')


def search(request):
    context = {}
    if request.session.get('user', False):
        if request.method == 'POST':
            value = request.POST['search']
            print(value)
            users = User.objects.filter(username__istartswith=value)
            context['users'] = users

            return render(request, 'facethemapp/search.html', context=context)
        else:
            return render(request, 'facethemapp/search.html', context=context)
    else:
        context['error'] = "You have to sign in :)"
        return render(request, 'facethemapp/error.html', context=context)


def settings(request):
    context = {}
    if request.session.get('user', False):
        return render(request, 'facethemapp/settings.html')
    else:
        context['error'] = "You have to sign in :)"
        return render(request, 'facethemapp/error.html', context=context)


'''Profile tabs'''


def about(request):
    return render(request, 'facethemapp/profile.html')


def stats(request):
    return render(request, 'facethemapp/stats.html')


def friends(request):
    return render(request, 'facethemapp/friends.html')
