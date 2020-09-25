from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Character, Equipment, AttackSpell, CharSpells
import json

# Create your views here.
def index(request):
    chars = list(Character.objects.all().order_by('-date'))
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
    c = get_object_or_404(Character, pk=character_id)
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
    return HttpResponse(str(character_id) + ' edit mode<br/><a href="send/">Submit</a>')

def submit_as(request, character_id):
    if request.is_ajax() and request.method == 'POST':
        # get json data
        data = json.loads(request.body)
        # get character
        c = get_object_or_404(Character, pk=character_id)
        if data['type'] == 'add':
            # check if name and character pair already exists
            atks = c.atks.filter(name=data['name'])
            if len(atks) > 0:
                return HttpResponse("Already exists")
            # make and save new attack/spell
            a = AttackSpell(character=c, name=data['name'], hit_dc=data['hit'], r=data['range'], damage=data['damage'])
            a.save()
        else:
            AttackSpell.objects.filter(name=data['name'], character=c).delete()
    return HttpResponse("OK")

def submit_eq(request, character_id):
    if request.is_ajax() and request.method == 'POST':
        # get json data
        data = json.loads(request.body)
        # get character
        c = get_object_or_404(Character, pk=character_id)
        if data['type'] == 'add':
            # check if name and character pair already exists
            eqs = c.equips.filter(name=data['name'])
            if len(eqs) > 0:
                return HttpResponse("Already exists")
            # make and save new attack/spell
            e = Equipment(character=c, name=data['name'], quantity=data['quantity'], weight=data['weight'])
            e.save()
        else:
            Equipment.objects.filter(name=data['name'], character=c).delete()
    return HttpResponse("OK")

def submit_sp(request, character_id):
    if request.is_ajax() and request.method == 'POST':
        # get json data
        data = json.loads(request.body)
        # get character
        c = get_object_or_404(Character, pk=character_id)
        if data['type'] == 'add':
            # check if name and character pair already exists
            spl = c.spls.filter(name=data['name'])
            if len(spl) > 0:
                return HttpResponse("Already exists")
            # make and save new attack/spell
            p = (data['prepared'] == 'true')
            s = CharSpells(character=c, name=data['name'], level=data['level'], prepared=p)
            s.save()
        else:
            CharSpells.objects.filter(name=data['name'], character=c).delete()
    return HttpResponse("OK")

def create(request):
    return HttpResponse('create mode')

def send_edit(request, character_id):
    return HttpResponseRedirect(reverse('cpage:char_page', args=(character_id,)))
