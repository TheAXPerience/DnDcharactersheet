from django.contrib.auth.models import User
from django.db import models, transaction
from django.utils import timezone

def check_overflow(val):
    val = int(val)
    if val > 2147483647:
        return 2147483647
    elif val < -2147483648:
        return -2147483648
    return val

# Create your models here.
class Character(models.Model):
    # implicit id for primary key
    name = models.CharField(max_length=50, default='n/a')
    creator = models.CharField(max_length=30, default='n/a') # keep for now as legacy
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    date = models.DateTimeField('creation date', default=timezone.now)

    # basic information
    char_class = models.CharField('class', max_length=20, default='n/a')
    level = models.IntegerField(default=1)
    bg = models.CharField('background', max_length=20, default='n/a')
    race = models.CharField(max_length=20, default='n/a')
    alignment = models.CharField(max_length=20, default='n/a')
    exp = models.IntegerField('experience', default=0)

    # important
    inspiration = models.BooleanField(default=False)
    proficiency_bonus = models.IntegerField(default=2)

    # health
    max_hp = models.IntegerField('maximum hit points', default=10)
    curr_hp = models.IntegerField('current hit points', default=10)
    temp_hp = models.IntegerField('temporary hit points', default=0)
    ds_success = models.IntegerField('death save successes', default=0)
    ds_failure = models.IntegerField('death save failures', default=0)

    # stats
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)

    # other numbers
    ac = models.IntegerField('armor class', default=0)
    initiative = models.IntegerField(default=0)
    movement = models.IntegerField('speed', default=30)

    # saving throw modifiers
    str_st = models.IntegerField('strength saving throw', default=0)
    dex_st = models.IntegerField('dexterity saving throw', default=0)
    con_st = models.IntegerField('constitution saving throw', default=0)
    int_st = models.IntegerField('intelligence saving throw', default=0)
    wsd_st = models.IntegerField('wisdom saving throw', default=0)
    chr_st = models.IntegerField('charisma saving throw', default=0)

    # saving throw proficiencies
    str_st_prof = models.BooleanField('strength saving throw proficiency', default=False)
    dex_st_prof = models.BooleanField('dexterity saving throw proficiency', default=False)
    con_st_prof = models.BooleanField('constitution saving throw proficiency', default=False)
    int_st_prof = models.BooleanField('intelligence saving throw proficiency', default=False)
    wsd_st_prof = models.BooleanField('wisdom saving throw proficiency', default=False)
    chr_st_prof = models.BooleanField('charisma saving throw proficiency', default=False)

    # skill modifiers
    acro = models.IntegerField('acrobatics', default=0)
    anha = models.IntegerField('animal handling', default=0)
    arca = models.IntegerField('arcana', default=0)
    athl = models.IntegerField('athletics', default=0)
    decp = models.IntegerField('deception', default=0)
    hist = models.IntegerField('history', default=0)
    insi = models.IntegerField('insight', default=0)
    intm = models.IntegerField('intimidation', default=0)
    invs = models.IntegerField('investigation', default=0)
    medi = models.IntegerField('medicine', default=0)
    natr = models.IntegerField('nature', default=0)
    perc = models.IntegerField('perception', default=0)
    perf = models.IntegerField('performance', default=0)
    pers = models.IntegerField('persuasion', default=0)
    rlgn = models.IntegerField('religion', default=0)
    sloh = models.IntegerField('sleight of hand', default=0)
    stea = models.IntegerField('stealth', default=0)
    surv = models.IntegerField('survival', default=0)

    acro_prf = models.BooleanField('acrobatics proficiency', default=False)
    anha_prf = models.BooleanField('animal handling proficiency', default=False)
    arca_prf = models.BooleanField('arcana proficiency', default=False)
    athl_prf = models.BooleanField('athletics proficiency', default=False)
    decp_prf = models.BooleanField('deception proficiency', default=False)
    hist_prf = models.BooleanField('history proficiency', default=False)
    insi_prf = models.BooleanField('insight proficiency', default=False)
    intm_prf = models.BooleanField('intimidation proficiency', default=False)
    invs_prf = models.BooleanField('investigation proficiency', default=False)
    medi_prf = models.BooleanField('medicine proficiency', default=False)
    natr_prf = models.BooleanField('nature proficiency', default=False)
    perc_prf = models.BooleanField('perception proficiency', default=False)
    perf_prf = models.BooleanField('performance proficiency', default=False)
    pers_prf = models.BooleanField('persuasion proficiency', default=False)
    rlgn_prf = models.BooleanField('religion proficiency', default=False)
    sloh_prf = models.BooleanField('sleight of hand proficiency', default=False)
    stea_prf = models.BooleanField('stealth proficiency', default=False)
    surv_prf = models.BooleanField('survival proficiency', default=False)

    pass_wsd = models.IntegerField('massive wisdom (perception)', default=0)

    # cash
    cp = models.FloatField('money (cp)', default=0)
    sp = models.FloatField('money (sp)', default=0)
    ep = models.FloatField('money (ep)', default=0)
    gp = models.FloatField('money (gp)', default=0)
    pp = models.FloatField('money (pp)', default=0)

    # spells stats
    spell_abl = models.CharField('spellcasting ability', max_length=10, default='n/a')
    spl_atk = models.IntegerField('spell attack bonus', default=0)
    spl_save = models.IntegerField('spell save dc', default=0)

    # spell slots
    lv1_slots = models.IntegerField('level 1 total slots', default=0)
    lv1_used = models.IntegerField('level 1 used slots', default=0)

    lv2_slots = models.IntegerField('level 2 total slots', default=0)
    lv2_used = models.IntegerField('level 2 used slots', default=0)

    lv3_slots = models.IntegerField('level 3 total slots', default=0)
    lv3_used = models.IntegerField('level 3 used slots', default=0)

    lv4_slots = models.IntegerField('level 4 total slots', default=0)
    lv4_used = models.IntegerField('level 4 used slots', default=0)

    lv5_slots = models.IntegerField('level 5 total slots', default=0)
    lv5_used = models.IntegerField('level 5 used slots', default=0)

    lv6_slots = models.IntegerField('level 6 total slots', default=0)
    lv6_used = models.IntegerField('level 6 used slots', default=0)

    lv7_slots = models.IntegerField('level 7 total slots', default=0)
    lv7_used = models.IntegerField('level 7 used slots', default=0)

    lv8_slots = models.IntegerField('level 8 total slots', default=0)
    lv8_used = models.IntegerField('level 8 used slots', default=0)

    lv9_slots = models.IntegerField('level 9 total slots', default=0)
    lv9_used = models.IntegerField('level 9 used slots', default=0)

    # text fields
    profs_lang = models.TextField('proficiencies and languages', default='Proficiencies, languages')
    feats_traits = models.TextField('features and traits', default='Features, traits')
    personality = models.TextField(default='ideals, bonds, flaws')
    backstory = models.TextField(default='character history, allies, organizations, etc.')
    appearance = models.TextField(default='hair, eye, skin, etc.')

    def queryset(self):
        return self.__class__.objects.filter(id=self.id)

    def verify_user(self, u):
        return u.id == self.user.id

    def getStats(self):
        return [
            {'name': 'Strength', 'stat': self.strength, 'bonus': int((self.strength - 10) / 2)},
            {'name': 'Dexterity', 'stat': self.dexterity, 'bonus': int((self.dexterity - 10) / 2)},
            {'name': 'Constitution', 'stat': self.constitution, 'bonus': int((self.constitution - 10) / 2)},
            {'name': 'Intelligence', 'stat': self.intelligence, 'bonus': int((self.intelligence - 10) / 2)},
            {'name': 'Wisdom', 'stat': self.wisdom, 'bonus': int((self.wisdom - 10) / 2)},
            {'name': 'Charisma', 'stat': self.charisma, 'bonus': int((self.charisma - 10) / 2)}
        ]
        """
        return {
            'str': (self.strength, self.str_st, self.str_st_prof),
            'dex': (self.dexterity, self.dex_st, self.dex_st_prof),
            'con': (self.constitution, self.con_st, self.con_st_prof),
            'int': (self.intelligence, self.int_st, self.int_st_prof),
            'wsd': (self.wisdom, self.wsd_st, self.wsd_st_prof),
            'chr': (self.charisma, self.chr_st, self.chr_st_prof)
        }"""

    def getStSkills(self):
        return [
            {'name': 'Strength', 'prf': self.str_st_prof, 'bonus': self.str_st},
            {'name': 'Acrobatics', 'prf': self.acro_prf, 'bonus': self.acro},
            {'name': 'Animal Handling', 'prf': self.anha_prf, 'bonus': self.anha},
            {'name': 'Arcana', 'prf': self.arca_prf, 'bonus': self.arca},
            {'name': 'Dexterity', 'prf': self.dex_st_prof, 'bonus': self.dex_st},
            {'name': 'Athletics', 'prf': self.athl_prf, 'bonus': self.athl},
            {'name': 'Deception', 'prf': self.decp_prf, 'bonus': self.decp},
            {'name': 'History', 'prf': self.hist_prf, 'bonus': self.hist},
            {'name': 'Constitution', 'prf': self.con_st_prof, 'bonus': self.con_st},
            {'name': 'Insight', 'prf': self.insi_prf, 'bonus': self.insi},
            {'name': 'Intimidation', 'prf': self.intm_prf, 'bonus': self.intm},
            {'name': 'Investigation', 'prf': self.invs_prf, 'bonus': self.invs},
            {'name': 'Intelligence', 'prf': self.int_st_prof, 'bonus': self.int_st},
            {'name': 'Medicine', 'prf': self.medi_prf, 'bonus': self.medi},
            {'name': 'Nature', 'prf': self.natr_prf, 'bonus': self.natr},
            {'name': 'Perception', 'prf': self.perc_prf, 'bonus': self.perc},
            {'name': 'Wisdom', 'prf': self.wsd_st_prof, 'bonus': self.wsd_st},
            {'name': 'Performance', 'prf': self.perf_prf, 'bonus': self.perf},
            {'name': 'Persuasion', 'prf': self.pers_prf, 'bonus': self.pers},
            {'name': 'Religion', 'prf': self.rlgn_prf, 'bonus': self.rlgn},
            {'name': 'Charisma', 'prf': self.chr_st_prof, 'bonus': self.chr_st},
            {'name': 'Sleight of Hand', 'prf': self.sloh_prf, 'bonus': self.sloh},
            {'name': 'Stealth', 'prf': self.stea_prf, 'bonus': self.stea},
            {'name': 'Survival', 'prf': self.surv_prf, 'bonus': self.surv}
        ]

    def getMoney(self):
        return [
            {'name': 'CP', 'value': self.cp},
            {'name': 'SP', 'value': self.sp},
            {'name': 'EP', 'value': self.ep},
            {'name': 'GP', 'value': self.gp},
            {'name': 'PP', 'value': self.pp}
        ]

    def getSpellSlots(self):
        return [
            {'lv': '1', 'used': self.lv1_used, 'total': self.lv1_slots},
            {'lv': '2', 'used': self.lv2_used, 'total': self.lv2_slots},
            {'lv': '3', 'used': self.lv3_used, 'total': self.lv3_slots},
            {'lv': '4', 'used': self.lv4_used, 'total': self.lv4_slots},
            {'lv': '5', 'used': self.lv5_used, 'total': self.lv5_slots},
            {'lv': '6', 'used': self.lv6_used, 'total': self.lv6_slots},
            {'lv': '7', 'used': self.lv7_used, 'total': self.lv7_slots},
            {'lv': '8', 'used': self.lv8_used, 'total': self.lv8_slots},
            {'lv': '9', 'used': self.lv9_used, 'total': self.lv9_slots}
        ]

    @transaction.atomic
    def edit_one(self, data):
        c = self.queryset().select_for_update().get()
        if (data['name'] == 'curr_hp'):
            c.curr_hp = check_overflow(data['data'])
        elif (data['name'] == 'temp_hp'):
            c.temp_hp = check_overflow(data['data'])
        elif (data['name'] == 'ds_success'):
            c.ds_success = check_overflow(data['data'])
        elif (data['name'] == 'ds_failure'):
            c.ds_failure = check_overflow(data['data'])
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
            c.lv1_used = check_overflow(data['data'])
        elif (data['name'] == 'lv2'):
            c.lv2_used = check_overflow(data['data'])
        elif (data['name'] == 'lv3'):
            c.lv3_used = check_overflow(data['data'])
        elif (data['name'] == 'lv4'):
            c.lv4_used = check_overflow(data['data'])
        elif (data['name'] == 'lv6'):
            c.lv6_used = check_overflow(data['data'])
        elif (data['name'] == 'lv5'):
            c.lv5_used = check_overflow(data['data'])
        elif (data['name'] == 'lv7'):
            c.lv7_used = check_overflow(data['data'])
        elif (data['name'] == 'lv8'):
            c.lv8_used = check_overflow(data['data'])
        elif (data['name'] == 'lv9'):
            c.lv9_used = check_overflow(data['data'])
        else:
            return 'Value not found'
        c.date = timezone.now()
        c.save()
        return 'OK'

    @transaction.atomic
    def edit_all(self, request):
        c = self.queryset().select_for_update().get()
        c.name = request.POST.get('charname')[:50]
        c.date = timezone.now()
        c.level = check_overflow(request.POST.get('level'))
        c.char_class = request.POST.get('charclass')[:20]
        c.race = request.POST.get('charrace')[:20]
        c.bg = request.POST.get('background')[:20]
        c.alignment = request.POST.get('alignment')[:20]
        c.exp = check_overflow(request.POST.get('exp'))
        c.strength = check_overflow(request.POST.get('str'))
        c.dexterity = check_overflow(request.POST.get('dex'))
        c.constitution = check_overflow(request.POST.get('con'))
        c.intelligence = check_overflow(request.POST.get('int'))
        c.wisdom = check_overflow(request.POST.get('wsd'))
        c.charisma = check_overflow(request.POST.get('chr'))
        c.inspiration = request.POST.get('inspiration') == 'on'
        c.proficiency_bonus = check_overflow(request.POST.get('prf'))
        c.pass_wsd = check_overflow(request.POST.get('passwsd'))
        c.ac = check_overflow(request.POST.get('armor'))
        c.initiative = check_overflow(request.POST.get('init'))
        c.movement = check_overflow(request.POST.get('move'))
        c.curr_hp = check_overflow(request.POST.get('currhp'))
        c.max_hp = check_overflow(request.POST.get('maxhp'))
        c.temp_hp = check_overflow(request.POST.get('temphp'))
        c.ds_success = check_overflow(request.POST.get('dss'))
        c.ds_failure = check_overflow(request.POST.get('dsf'))
        c.str_st_prof = request.POST.get('strst_prf') == 'on'
        c.str_st = check_overflow(request.POST.get('strst'))
        c.dex_st_prof = request.POST.get('dexst_prf') == 'on'
        c.dex_st = check_overflow(request.POST.get('dexst'))
        c.con_st_prof = request.POST.get('const_prf') == 'on'
        c.con_st = check_overflow(request.POST.get('const'))
        c.int_st_prof = request.POST.get('intst_prf') == 'on'
        c.int_st = check_overflow(request.POST.get('intst'))
        c.wsd_st_prof = request.POST.get('wsdst_prf') == 'on'
        c.wsd_st = check_overflow(request.POST.get('wsdst'))
        c.chr_st_prof = request.POST.get('chrst_prf') == 'on'
        c.chr_st = check_overflow(request.POST.get('chrst'))
        c.acro_prf = request.POST.get('acro_prf') == 'on'
        c.acro = check_overflow(request.POST.get('acro'))
        c.anha_prf = request.POST.get('anha_prf') == 'on'
        c.anha = check_overflow(request.POST.get('anha'))
        c.arca_prf = request.POST.get('arca_prf') == 'on'
        c.arca = check_overflow(request.POST.get('arca'))
        c.athl_prf = request.POST.get('athl_prf') == 'on'
        c.athl = check_overflow(request.POST.get('athl'))
        c.decp_prf = request.POST.get('decp_prf') == 'on'
        c.decp = check_overflow(request.POST.get('decp'))
        c.hist_prf = request.POST.get('hist_prf') == 'on'
        c.hist = check_overflow(request.POST.get('hist'))
        c.insi_prf = request.POST.get('insi_prf') == 'on'
        c.insi = check_overflow(request.POST.get('insi'))
        c.intm_prf = request.POST.get('intm_prf') == 'on'
        c.intm = check_overflow(request.POST.get('intm'))
        c.invs_prf = request.POST.get('invs_prf') == 'on'
        c.invs = check_overflow(request.POST.get('invs'))
        c.medi_prf = request.POST.get('medi_prf') == 'on'
        c.medi = check_overflow(request.POST.get('medi'))
        c.natr_prf = request.POST.get('natr_prf') == 'on'
        c.natr = check_overflow(request.POST.get('natr'))
        c.perf_prf = request.POST.get('perf_prf') == 'on'
        c.perf = check_overflow(request.POST.get('perf'))
        c.perc_prf = request.POST.get('perc_prf') == 'on'
        c.perc = check_overflow(request.POST.get('perc'))
        c.pers_prf = request.POST.get('pers_prf') == 'on'
        c.pers = check_overflow(request.POST.get('pers'))
        c.rlgn_prf = request.POST.get('rlgn_prf') == 'on'
        c.rlgn = check_overflow(request.POST.get('rlgn'))
        c.sloh_prf = request.POST.get('sloh_prf') == 'on'
        c.sloh = check_overflow(request.POST.get('sloh'))
        c.stea_prf = request.POST.get('stea_prf') == 'on'
        c.stea = check_overflow(request.POST.get('stea'))
        c.surv_prf = request.POST.get('surv_prf') == 'on'
        c.surv = check_overflow(request.POST.get('surv'))
        c.cp = request.POST.get('cp')
        c.sp = request.POST.get('sp')
        c.ep = request.POST.get('ep')
        c.gp = request.POST.get('gp')
        c.pp = request.POST.get('pp')
        c.spell_abl = request.POST.get('spl_abl')[:10]
        c.spl_save = check_overflow(request.POST.get('spl_save'))
        c.spl_atk = check_overflow(request.POST.get('spl_atk'))
        c.lv1_used = check_overflow(request.POST.get('lv1_used'))
        c.lv1_slots = check_overflow(request.POST.get('lv1_ttl'))
        c.lv2_used = check_overflow(request.POST.get('lv2_used'))
        c.lv2_slots = check_overflow(request.POST.get('lv2_ttl'))
        c.lv3_used = check_overflow(request.POST.get('lv3_used'))
        c.lv3_slots = check_overflow(request.POST.get('lv3_ttl'))
        c.lv4_used = check_overflow(request.POST.get('lv4_used'))
        c.lv4_slots = check_overflow(request.POST.get('lv4_ttl'))
        c.lv5_used = check_overflow(request.POST.get('lv5_used'))
        c.lv5_slots = check_overflow(request.POST.get('lv5_ttl'))
        c.lv6_used = check_overflow(request.POST.get('lv6_used'))
        c.lv6_slots = check_overflow(request.POST.get('lv6_ttl'))
        c.lv7_used = check_overflow(request.POST.get('lv7_used'))
        c.lv7_slots = check_overflow(request.POST.get('lv7_ttl'))
        c.lv8_used = check_overflow(request.POST.get('lv8_used'))
        c.lv8_slots = check_overflow(request.POST.get('lv8_ttl'))
        c.lv9_used = check_overflow(request.POST.get('lv9_used'))
        c.lv9_slots = check_overflow(request.POST.get('lv9_ttl'))
        c.profs_lang = request.POST.get('prf_lang')
        c.feats_traits = request.POST.get('ft_trt')
        c.personality = request.POST.get('personality')
        c.backstory = request.POST.get('backstory')
        c.appearance = request.POST.get('appearance')
        c.save()

    @transaction.atomic
    def add_AS(self, data):
        c = self.queryset().select_for_update().get()
        if data['type'] == 'add':
            # check if name and character pair already exists
            atks = c.atks.filter(name=data['name'])
            if len(atks) > 0:
                return 'This attack already exists'
            # make and save new attack/spell
            a = AttackSpell(
                character=c,
                name=data['name'][:30],
                hit_dc=data['hit'][:10],
                r=check_overflow(data['range']),
                damage=data['damage'][:20]
            )
            a.save()
            c.date = timezone.now()
            c.save()
        else:
            AttackSpell.objects.filter(name=data['name'], character=c).delete()
        return 'OK'

    @transaction.atomic
    def add_EQ(self, data):
        c = self.queryset().select_for_update().get()
        if data['type'] == 'add':
            # check if name and character pair already exists
            eqs = c.equips.filter(name=data['name'])
            if len(eqs) > 0:
                return 'Error: equipment already exists'
            # make and save new attack/spell
            e = Equipment(
                character=c,
                name=data['name'][:50],
                quantity=check_overflow(data['quantity']),
                weight=data['weight']
            )
            e.save()
            c.date = timezone.now()
            c.save()
        else:
            Equipment.objects.filter(name=data['name'], character=c).delete()
        return 'OK'

    @transaction.atomic
    def add_SP(self, data):
        c = self.queryset().select_for_update().get()
        if data['type'] == 'add':
            # check if name and character pair already exists
            spl = c.spls.filter(name=data['name'])
            if len(spl) > 0:
                return 'This spell already exists'
            # make and save new attack/spell
            p = (data['prepared'] == 'true')
            s = CharSpells(
                character=c,
                name=data['name'][:30],
                level=check_overflow(data['level']),
                prepared=p
            )
            s.save()
            c.date = timezone.now()
            c.save()
        else:
            CharSpells.objects.filter(name=data['name'], character=c).delete()
        return 'OK'

class Equipment(models.Model):
    character = models.ForeignKey(Character, null=True, on_delete=models.CASCADE, related_name='equips')
    name = models.CharField('equipment', max_length=50, default='n/a')
    quantity = models.IntegerField(default=1)
    weight = models.FloatField(default=1)

    class Meta:
        unique_together = (('character', 'name'),)

class AttackSpell(models.Model):
    character = models.ForeignKey(Character, null=True, on_delete=models.CASCADE, related_name='atks')
    name = models.CharField('name', max_length=30, default='n/a')
    hit_dc = models.CharField('hit/dc', max_length=10, default='0')
    r = models.IntegerField('range', default=5)
    damage = models.CharField('damage/type', max_length=20, default='n/a')

    class Meta:
        unique_together = (('character', 'name'),)

class CharSpells(models.Model):
    character = models.ForeignKey(Character, null=True, on_delete=models.CASCADE, related_name='spls')
    name = models.CharField('spell name', max_length=30, default='n/a')
    level = models.IntegerField(default=0)
    prepared = models.BooleanField(default=False)

    class Meta:
        unique_together = (('character', 'name'),)

class Favorite(models.Model):
    character = models.ForeignKey(Character, null=False, on_delete=models.CASCADE, related_name='faved')
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='favor')
    date = models.DateTimeField('favorite date', default=timezone.now)
