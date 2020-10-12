from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Character, Equipment, AttackSpell, CharSpells, Favorite
import json

# Create your views here.
def index(request):
    context = {}
    with transaction.atomic():
        chars = list(Character.objects.select_for_update().all().order_by('-date'))
        pages = [1]
        if len(chars) > 25:
            pages.append(2)
        if len(chars) > 50:
            pages.append(3)
        lst = int((len(chars) - 1) / 25) + 1
        context = {
            'characters': chars[:25],
            'prv': 1,
            'nxt': min(lst, 2),
            'pages': pages,
            'lst': lst,
            'no_one': 1,
            'no_two': min(25, len(chars)),
            'no_three': len(chars),
            'user': request.user,
        }
    return render(request, 'characterpage/index.html', context)

def page(request, page):
    if page < 1:
        return page(request, 1)
    context = {}
    with transaction.atomic():
        chars = list(Character.objects.all().order_by('-date'))
        no_one = 1 + (page - 1) * 25
        no_two = min(page * 25, len(chars))
        lst = int((len(chars) - 1) / 25) + 1
        pages = list(range(page-2, page+3))
        while pages[0] < 1:
            pages.pop(0)
        while pages[-1] > lst:
            pages.pop()
        context = {
            'user': request.user,
            'characters': chars[no_one-1:no_two],
            'prv': max(1, page - 1),
            'nxt': min(lst, page + 1),
            'pages': pages,
            'lst': lst,
            'no_one': no_one,
            'no_two': no_two,
            'no_three': len(chars)
        }
    return render(request, 'characterpage/index.html', context)


def character(request, character_id):
    context = {}
    with transaction.atomic():
        c = get_object_or_404(Character.objects.select_for_update(), pk=character_id)
        a = list(c.atks.all())
        e = list(c.equips.all())
        s = list(c.spls.all())
        if a == None or len(a) == 0:
            a = None
        if e == None or len(e) == 0:
            e = None
        if s == None or len(s) == 0:
            s = None
        context = {
            'user': request.user,
            'is_user': request.user.is_authenticated and request.user == c.user,
            'character': c,
            'atk': a,
            'eqp': e,
            'spls': s
        }
    return render(request, 'characterpage/character.html', context)

def edit(request, character_id):
    context = {}
    if not request.user.is_authenticated:
        # not allowed to access edit page
        return HttpResponseRedirect(reverse('cpage:index'))
    with transaction.atomic():
        c = get_object_or_404(Character.objects.select_for_update(), pk=character_id)
        if not request.user == c.user:
            # only the original user can edit their own character
            return HttpResponseRedirect(reverse('cpage:index'))
        context = {
            'user': request.user,
            'character': c,
        }
    return render(request, 'characterpage/submit.html', context)

def check_overflow(val):
    val = int(val)
    if val > 2147483647:
        return 2147483647
    elif val < -2147483648:
        return -2147483648
    return val

def submit_edit(request, character_id):
    if request.is_ajax() and request.method == 'POST':
        data = json.loads(request.body)
        c = get_object_or_404(Character, pk=character_id)
        return HttpResponse(c.edit_one(data))
    return HttpResponse('OK')

def submit_as(request, character_id):
    if request.is_ajax() and request.method == 'POST':
        # get json data
        data = json.loads(request.body)
        # get character
        c = get_object_or_404(Character, pk=character_id)
        return HttpResponse(c.add_AS(data))
    return HttpResponse("OK")

def submit_eq(request, character_id):
    if request.is_ajax() and request.method == 'POST':
        # get json data
        data = json.loads(request.body)
        # get character
        c = get_object_or_404(Character, pk=character_id)
        return HttpResponse(c.add_EQ(data))
    return HttpResponse("OK")

def submit_sp(request, character_id):
    if request.is_ajax() and request.method == 'POST':
        # get json data
        data = json.loads(request.body)
        # get character
        c = get_object_or_404(Character, pk=character_id)
        return HttpResponse(c.add_SP(data))
    return HttpResponse("OK")

def create(request):
    if not request.user.is_authenticated:
        # not allowed to make a character
        return HttpResponseRedirect(reverse('cpage:index'))
    c = Character(date = timezone.now(), user=request.user)
    c.save()
    return HttpResponseRedirect(reverse('cpage:char_edit', args=(c.id,)))

def send_edit(request, character_id):
    c = get_object_or_404(Character, pk=character_id)
    c.edit_all(request)
    return HttpResponseRedirect(reverse('cpage:char_page', args=(character_id,)))

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

# login to an account
def login_account(request):
    # passed username and password as json
    # must authenticate user
    username = ''
    password = ''
    if request.is_ajax() and request.method == 'POST':
        # grab json data
        data = json.loads(request.body)
        # save json data
        username = data['username']
        password = data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse('OK')
    else:
        return HttpResponse('Error: username and password not recognized.')

# logout of an account
def logout_account(request):
    logout(request)
    return HttpResponseRedirect(reverse('cpage:index'))

# create an account
def create_account(request):
    username = ''
    password = ''
    email = ''
    if request.is_ajax() and request.method == 'POST':
        # grab json data
        data = json.loads(request.body)
        # save json data
        username = data['username']
        password = data['password']
        email = data['email']
    else:
        return HttpResponse('Error: request invalid.')
    other_user = User.objects.filter(username=username)
    if len(other_user) > 0:
        return HttpResponse('Error: username already exists.')
    # password check
    if validate_password(password) is not None:
        return HttpResponse('Error: password invalid.<br/>Passowrd must be 4 characters minimum.<br/>Password must not be entirely numeric.')
    user = User(username=username, email=email, password=make_password(password))
    user.save()
    login(request, user)
    return HttpResponse('OK')

def profile_page(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': user,
        'characters': Character.objects.filter(user=user).order_by('-date'),
        'favorites': Favorite.objects.filter(user=user).order_by('-date'),
        'user_me': request.user
    }
    return render(request, 'characterpage/profile.html', context)

def add_to_favorites(request, character_id):
    if request.is_ajax() and request.method='POST':
        if not request.user.is_authenticated:
            return HttpResponse('Error: user not signed in.')
        with transaction.atomic():
            c = get_object_or_404(Character.objects.select_for_update(), pk=character_id)
            favs = Favorite.objects.filter(user=request.user, character=c)
            if len(favs) > 0:
                return HttpResponse('Error: character already added to favorites.')
            favorite = Favorite(date=timezone.now(), user=request.user, character=c)
            favorite.save()
    return HttpResponse('OK')

def remove_from_favorites(request, character_id):
    if request.is_ajax() and request.method='POST':
        if not request.user.is_authenticated:
            return HttpResponse('Error: user not signed in.')
        with transaction.atomic():
            c = get_object_or_404(Character.objects.select_for_update(), pk=character_id)
            favs = Favorite.objects.filter(user=request.user, character=c)
            if len(favs) != 1:
                return HttpResponse('Error: character already not in favorites.')
            favs.delete()
    return HttpResponse('OK')
