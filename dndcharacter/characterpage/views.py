from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
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
    c = get_object_or_404(Character, pk=character_id)
    context = {
        'character': c
    }
    return render(request, 'characterpage/submit.html', context)

def submit_edit(request, character_id):
    if request.is_ajax() and request.method == 'POST':
        data = json.loads(request.body)
        c = get_object_or_404(Character, pk=character_id)
        # very long if / elif chain bc python has no freakin' switch statements
        if (data['name'] == 'curr_hp'):
            c.curr_hp = data['data']
        elif (data['name'] == 'temp_hp'):
            c.temp_hp = data['data']
        elif (data['name'] == 'ds_success'):
            c.ds_success = data['data']
        elif (data['name'] == 'ds_failure'):
            c.ds_failure = data['data']
        elif (data['name'] == 'CP'):
            c.cp = data['data']
        elif (data['name'] == 'EP'):
            c.ep = data['data']
        elif (data['name'] == 'SP'):
            c.sp = data['data']
        elif (data['name'] == 'GP'):
            c.gp = data['data']
        elif (data['name'] == 'PP'):
            c.pp = data['data']
        elif (data['name'] == 'lv1'):
            c.lv1_used = data['data']
        elif (data['name'] == 'lv2'):
            c.lv2_used = data['data']
        elif (data['name'] == 'lv3'):
            c.lv3_used = data['data']
        elif (data['name'] == 'lv4'):
            c.lv4_used = data['data']
        elif (data['name'] == 'lv6'):
            c.lv6_used = data['data']
        elif (data['name'] == 'lv5'):
            c.lv5_used = data['data']
        elif (data['name'] == 'lv7'):
            c.lv7_used = data['data']
        elif (data['name'] == 'lv8'):
            c.lv8_used = data['data']
        elif (data['name'] == 'lv1'):
            c.lv1_used = data['data']
        elif (data['name'] == 'lv9'):
            c.lv9_used = data['data']
        else:
            return HttpResponse('Value not found')
        c.date = timezone.now()
        c.save()
    return HttpResponse('OK')

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
            c.date = timezone.now()
            c.save()
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
            c.date = timezone.now()
            c.save()
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
            c.date = timezone.now()
            c.save()
        else:
            CharSpells.objects.filter(name=data['name'], character=c).delete()
    return HttpResponse("OK")

def create(request):
    return HttpResponse('create mode')

def send_edit(request, character_id):
    c = get_object_or_404(Character, pk=character_id)
    c.name = request.POST.get('charname')
    c.date = timezone.now()
    c.level = request.POST.get('level')
    c.char_class = request.POST.get('charclass')
    c.race = request.POST.get('charrace')
    c.creator = request.POST.get('player')
    c.bg = request.POST.get('background')
    c.alignment = request.POST.get('alignment')
    c.exp = request.POST.get('exp')
    c.strength = request.POST.get('str')
    c.dexterity = request.POST.get('dex')
    c.constitution = request.POST.get('con')
    c.intelligence = request.POST.get('int')
    c.wisdom = request.POST.get('wsd')
    c.charisma = request.POST.get('chr')
    c.inspiration = request.POST.get('inspiration') == 'on'
    c.proficiency_bonus = request.POST.get('prf')
    c.pass_wsd = request.POST.get('passwsd')
    c.ac = request.POST.get('armor')
    c.initiative = request.POST.get('init')
    c.movement = request.POST.get('move')
    c.curr_hp = request.POST.get('currhp')
    c.max_hp = request.POST.get('maxhp')
    c.temp_hp = request.POST.get('temphp')
    c.ds_success = request.POST.get('dss')
    c.ds_failure = request.POST.get('dsf')
    c.str_st_prof = request.POST.get('strst_prf') == 'on'
    c.str_st = request.POST.get('strst')
    c.dex_st_prof = request.POST.get('dexst_prf') == 'on'
    c.dex_st = request.POST.get('dexst')
    c.con_st_prof = request.POST.get('const_prf') == 'on'
    c.con_st = request.POST.get('const')
    c.int_st_prof = request.POST.get('intst_prf') == 'on'
    c.int_st = request.POST.get('intst')
    c.wsd_st_prof = request.POST.get('wsdst_prf') == 'on'
    c.wsd_st = request.POST.get('wsdst')
    c.chr_st_prof = request.POST.get('chrst_prf') == 'on'
    c.chr_st = request.POST.get('chrst')
    c.acro_prf = request.POST.get('acro_prf') == 'on'
    c.acro = request.POST.get('acro')
    c.anha_prf = request.POST.get('anha_prf') == 'on'
    c.anha = request.POST.get('anha')
    c.arca_prf = request.POST.get('arca_prf') == 'on'
    c.arca = request.POST.get('arca')
    c.athl_prf = request.POST.get('athl_prf') == 'on'
    c.athl = request.POST.get('athl')
    c.decp_prf = request.POST.get('decp_prf') == 'on'
    c.decp = request.POST.get('decp')
    c.hist_prf = request.POST.get('hist_prf') == 'on'
    c.hist = request.POST.get('hist')
    c.insi_prf = request.POST.get('insi_prf') == 'on'
    c.insi = request.POST.get('insi')
    c.intm_prf = request.POST.get('intm_prf') == 'on'
    c.intm = request.POST.get('intm')
    c.invs_prf = request.POST.get('invs_prf') == 'on'
    c.invs = request.POST.get('invs')
    c.medi_prf = request.POST.get('medi_prf') == 'on'
    c.medi = request.POST.get('medi')
    c.natr_prf = request.POST.get('natr_prf') == 'on'
    c.natr = request.POST.get('natr')
    c.perf_prf = request.POST.get('perf_prf') == 'on'
    c.perf = request.POST.get('perf')
    c.perc_prf = request.POST.get('perc_prf') == 'on'
    c.perc = request.POST.get('perc')
    c.pers_prf = request.POST.get('pers_prf') == 'on'
    c.pers = request.POST.get('pers')
    c.rlgn_prf = request.POST.get('rlgn_prf') == 'on'
    c.rlgn = request.POST.get('rlgn')
    c.sloh_prf = request.POST.get('sloh_prf') == 'on'
    c.sloh = request.POST.get('sloh')
    c.stea_prf = request.POST.get('stea_prf') == 'on'
    c.stea = request.POST.get('stea')
    c.surv_prf = request.POST.get('surv_prf') == 'on'
    c.surv = request.POST.get('surv')
    c.cp = request.POST.get('cp')
    c.sp = request.POST.get('sp')
    c.ep = request.POST.get('ep')
    c.gp = request.POST.get('gp')
    c.pp = request.POST.get('pp')
    c.spell_abl = request.POST.get('spl_abl')
    c.spl_save = request.POST.get('spl_save')
    c.spl_atk = request.POST.get('spl_atk')
    c.lv1_used = request.POST.get('lv1_used')
    c.lv1_slots = request.POST.get('lv1_ttl')
    c.lv2_used = request.POST.get('lv2_used')
    c.lv2_slots = request.POST.get('lv2_ttl')
    c.lv3_used = request.POST.get('lv3_used')
    c.lv3_slots = request.POST.get('lv3_ttl')
    c.lv4_used = request.POST.get('lv4_used')
    c.lv4_slots = request.POST.get('lv4_ttl')
    c.lv5_used = request.POST.get('lv5_used')
    c.lv5_slots = request.POST.get('lv5_ttl')
    c.lv6_used = request.POST.get('lv6_used')
    c.lv6_slots = request.POST.get('lv6_ttl')
    c.lv7_used = request.POST.get('lv7_used')
    c.lv7_slots = request.POST.get('lv7_ttl')
    c.lv8_used = request.POST.get('lv8_used')
    c.lv8_slots = request.POST.get('lv8_ttl')
    c.lv9_used = request.POST.get('lv9_used')
    c.lv9_slots = request.POST.get('lv9_ttl')
    c.profs_lang = request.POST.get('prf_lang')
    c.feats_traits = request.POST.get('ft_trt')
    c.personality = request.POST.get('personality')
    c.backstory = request.POST.get('backstory')
    c.appearance = request.POST.get('appearance')
    c.save()
    return HttpResponseRedirect(reverse('cpage:char_page', args=(character_id,)))
