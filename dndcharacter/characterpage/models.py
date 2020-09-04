from django.db import models
from django.utils import timezone

# Create your models here.
class Character(models.Model):
    # implicit id for primary key
    name = models.CharField(max_length=50, default='n/a')
    creator = models.CharField(max_length=30, default='n/a')
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

    def getStats(self):
        return {
            'str': (self.strength, self.str_st, self.str_st_prof),
            'dex': (self.dexterity, self.dex_st, self.dex_st_prof),
            'con': (self.constitution, self.con_st, self.con_st_prof),
            'int': (self.intelligence, self.int_st, self.int_st_prof),
            'wsd': (self.wisdom, self.wsd_st, self.wsd_st_prof),
            'chr': (self.charisma, self.chr_st, self.chr_st_prof)
        }

    def getSkills(self):
        return {
            'acro': (self.acro, self.acro_prf),
            'anha': (self.anha, self.anha_prf),
            'arca': (self.arca, self.arca_prf),
            'athl': (self.athl, self.athl_prf),
            'decp': (self.decp, self.decp_prf),
            'hist': (self.hist, self.hist_prf),
            'insi': (self.insi, self.insi_prf),
            'intm': (self.intm, self.intm_prf),
            'invs': (self.invs, self.invs_prf),
            'medi': (self.medi, self.medi_prf),
            'natr': (self.natr, self.natr_prf),
            'perc': (self.perc, self.perc_prf),
            'perf': (self.perf, self.perf_prf),
            'pers': (self.pers, self.pers_prf),
            'rlgn': (self.rlgn, self.rlgn_prf),
            'sloh': (self.sloh, self.sloh_prf),
            'stea': (self.stea, self.stea_prf),
            'surv': (self.surv, self.surv_prf)
        }

    def getSpellSlots(self):
        return [
            (self.lv1_used, self.lv1_slots),
            (self.lv2_used, self.lv2_slots),
            (self.lv3_used, self.lv3_slots),
            (self.lv4_used, self.lv4_slots),
            (self.lv5_used, self.lv5_slots),
            (self.lv6_used, self.lv6_slots),
            (self.lv7_used, self.lv7_slots),
            (self.lv8_used, self.lv8_slots),
            (self.lv9_used, self.lv9_slots)
        ]

class Equipment(models.Model):
    character = models.ForeignKey(Character, null=True, on_delete=models.CASCADE, related_name='owner')
    name = models.CharField('equipment', max_length=50, default='')
    quantity = models.IntegerField(default=1)
    weight = models.FloatField(default=1)

    class Meta:
        unique_together = (('character', 'name'),)

class AttackSpell(models.Model):
    character = models.ForeignKey(Character, null=True, on_delete=models.CASCADE, related_name='attacker')
    name = models.CharField('attack name', max_length=30, default='')
    hit_dc = models.CharField('hit/dc', max_length=10, default='0')
    r = models.IntegerField('range', default=5)
    damage = models.CharField('damage/type', max_length=20, default='')

    class Meta:
        unique_together = (('character', 'name'),)

class CharSpells(models.Model):
    character = models.ForeignKey(Character, null=True, on_delete=models.CASCADE, related_name='caster')
    name = models.CharField('Spell Name', max_length=30, default='')
    level = models.IntegerField(default=0)
    prepared = models.BooleanField(default=False)

    class Meta:
        unique_together = (('character', 'name'),)
