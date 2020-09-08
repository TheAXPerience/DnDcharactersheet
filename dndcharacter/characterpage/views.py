from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Character, Equipment, AttackSpell, CharSpells

# Create your views here.
def index(request):
    ret = '<a href="create/">Create</a><br/>'
    chars = list(Character.objects.all())
    for c in chars:
        ret = ret + '<a href="character/' + str(c.id) + '">' + c.name + ' and ' + c.creator + '</a><br/>'
    return HttpResponse(ret);

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
    return render(request, 'characterpage/character.html', context);

def edit(request, character_id):
    return HttpResponse(str(character_id) + ' edit mode<br/><a href="send/">Submit</a>')

def create(request):
    return HttpResponse('create mode')

def send_edit(request, character_id):
    return HttpResponseRedirect(reverse('cpage:char_page', args=(character_id,)))
