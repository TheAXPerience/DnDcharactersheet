from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Character, Equipment, AttackSpell, CharSpells
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
            'no_three': len(chars)
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
            'character': c,
            'atk': a,
            'eqp': e,
            'spls': s
        }
    return render(request, 'characterpage/character.html', context)

def edit(request, character_id):
    context = {}
    with transaction.atomic():
        c = get_object_or_404(Character.objects.select_for_update(), pk=character_id)
        context = {
            'character': c
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
    c = Character(date = timezone.now())
    c.save()
    return HttpResponseRedirect(reverse('cpage:char_edit', args=(c.id,)))

def send_edit(request, character_id):
    c = get_object_or_404(Character, pk=character_id)
    c.edit_all(request)
    return HttpResponseRedirect(reverse('cpage:char_page', args=(character_id,)))
