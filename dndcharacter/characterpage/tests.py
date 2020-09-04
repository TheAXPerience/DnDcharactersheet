from django.test import TestCase
from .models import Character
from django.utils import timezone
from django.core import exceptions
import datetime

# Create your tests here.
class CharacterCreationTestcase(TestCase):
    def setUp(self):
        Character.objects.create(name='henry', creator='kevin')
        Character.objects.create(name='Perfect', creator='kevin')
        Character.objects.create(name='1', creator='y', date=datetime.datetime(2000, 1, 1))
        Character.objects.create(name='4', creator='y', date=datetime.datetime(2001, 1, 1))
        Character.objects.create(name='2', creator='y', date=datetime.datetime(2002, 1, 1))
        Character.objects.create(name='5', creator='y', date=datetime.datetime(2003, 1, 1))
        Character.objects.create(name='3', creator='y', date=datetime.datetime(2004, 1, 1))
        Character.objects.create(
            name='Pan Bastian Edge',
            creator='Alvin',
            char_class='Bard',
            level='2',
            bg='Criminal/Spy',
            race='Aarakocra',
            alignment='Chaotic Neutral',
            exp=10,
            inspiration=True,
            proficiency_bonus=3,
            max_hp=15,
            curr_hp=15,
            temp_hp=1,
            ds_success=1,
            ds_failure=1,
            strength=15,
            dexterity=15,
            constitution=15,
            intelligence=15,
            wisdom=15,
            charisma=15,
            ac=12,
            initiative=3,
            movement=25,
            str_st=1,
            dex_st=1,
            con_st=1,
            int_st=1,
            wsd_st=1,
            chr_st=1,
            str_st_prof=True,
            dex_st_prof=True,
            con_st_prof=True,
            int_st_prof=True,
            wsd_st_prof=True,
            chr_st_prof=True,
            acro=1,
            anha=1,
            arca=1,
            athl=1,
            decp=1,
            hist=1,
            insi=1,
            intm=1,
            invs=1,
            medi=1,
            natr=1,
            perc=1,
            perf=1,
            pers=1,
            rlgn=1,
            sloh=1,
            stea=1,
            surv=1,
            acro_prf=True,
            anha_prf=True,
            arca_prf=True,
            athl_prf=True,
            decp_prf=True,
            hist_prf=True,
            insi_prf=True,
            intm_prf=True,
            invs_prf=True,
            medi_prf=True,
            natr_prf=True,
            perc_prf=True,
            perf_prf=True,
            pers_prf=True,
            rlgn_prf=True,
            sloh_prf=True,
            stea_prf=True,
            surv_prf=True,
            pass_wsd=13,
            cp=1,
            sp=1,
            ep=1,
            gp=1,
            pp=1,
            spell_abl='Charisma',
            spl_atk=4,
            spl_save=14,
            lv1_slots=3,
            lv1_used=1,
            lv2_slots=3,
            lv2_used=1,
            lv3_slots=3,
            lv3_used=1,
            lv4_slots=3,
            lv4_used=1,
            lv5_slots=3,
            lv5_used=1,
            lv6_slots=3,
            lv6_used=1,
            lv7_slots=3,
            lv7_used=1,
            lv8_slots=3,
            lv8_used=1,
            lv9_slots=3,
            lv9_used=1,
            profs_lang='yes',
            feats_traits='no',
            personality='maybe',
            backstory='so',
            appearance='birb'
        )
        Character.objects.create(
            name='omfg',
            strength=15,
            dexterity=15,
            constitution=15,
            intelligence=15,
            wisdom=15,
            charisma=15,
            str_st=1,
            dex_st=1,
            con_st=1,
            int_st=1,
            wsd_st=1,
            chr_st=1,
            str_st_prof=True,
            dex_st_prof=True,
            con_st_prof=True,
            int_st_prof=True,
            wsd_st_prof=True,
            chr_st_prof=True,
            acro=1,
            anha=1,
            arca=1,
            athl=1,
            decp=1,
            hist=1,
            insi=1,
            intm=1,
            invs=1,
            medi=1,
            natr=1,
            perc=1,
            perf=1,
            pers=1,
            rlgn=1,
            sloh=1,
            stea=1,
            surv=1,
            acro_prf=True,
            anha_prf=True,
            arca_prf=True,
            athl_prf=True,
            decp_prf=True,
            hist_prf=True,
            insi_prf=True,
            intm_prf=True,
            invs_prf=True,
            medi_prf=True,
            natr_prf=True,
            perc_prf=True,
            perf_prf=True,
            pers_prf=True,
            rlgn_prf=True,
            sloh_prf=True,
            stea_prf=True,
            surv_prf=True,
            lv1_slots=3,
            lv1_used=1,
            lv2_slots=3,
            lv2_used=1,
            lv3_slots=3,
            lv3_used=1,
            lv4_slots=3,
            lv4_used=1,
            lv5_slots=3,
            lv5_used=1,
            lv6_slots=3,
            lv6_used=1,
            lv7_slots=3,
            lv7_used=1,
            lv8_slots=3,
            lv8_used=1,
            lv9_slots=3,
            lv9_used=1
        )

    def test_setup(self):
        self.assertEqual(9, Character.objects.count())
    
    # test the default setup
    def test_default_setup(self):
        d = timezone.now()
        c = Character(date=d) # would be tricky to exact test the default value if set to now
        self.assertEqual(c.name, 'n/a')
        self.assertEqual(c.creator, 'n/a')
        self.assertEqual(c.date, d)
        
        self.assertEqual(c.char_class, 'n/a')
        self.assertEqual(c.level, 1)
        self.assertEqual(c.bg, 'n/a')
        self.assertEqual(c.race, 'n/a')
        self.assertEqual(c.alignment, 'n/a')
        self.assertEqual(c.exp, 0)
        self.assertEqual(c.inspiration, False)
        self.assertEqual(c.proficiency_bonus, 2)
        
        self.assertEqual(c.max_hp, 10)
        self.assertEqual(c.curr_hp, 10)
        self.assertEqual(c.temp_hp, 0)
        self.assertEqual(c.ds_success, 0)
        self.assertEqual(c.ds_failure, 0)
        
        self.assertEqual(c.ac, 0)
        self.assertEqual(c.initiative, 0)
        self.assertEqual(c.movement, 30)
        self.assertEqual(c.pass_wsd, 0)
        
        self.assertEqual(c.cp, 0)
        self.assertEqual(c.sp, 0)
        self.assertEqual(c.ep, 0)
        self.assertEqual(c.gp, 0)
        self.assertEqual(c.pp, 0)
        
        self.assertEqual(c.spell_abl, 'n/a')
        self.assertEqual(c.spl_atk, 0)
        self.assertEqual(c.spl_save, 0)
        self.assertEqual(c.profs_lang, 'Proficiencies, languages')
        self.assertEqual(c.feats_traits, 'Features, traits')
        self.assertEqual(c.personality, 'ideals, bonds, flaws')
        self.assertEqual(c.backstory, 'character history, allies, organizations, etc.')
        self.assertEqual(c.appearance, 'hair, eye, skin, etc.')

        stats = c.getStats()
        for k in stats:
            x, y, z = stats[k]
            self.assertEqual(x, 10)
            self.assertEqual(y, 0)
            self.assertEqual(z, False)

        skills = c.getSkills()
        for k in skills:
            a, b = skills[k]
            self.assertEqual(a, 0)
            self.assertEqual(b, False)

        slots = c.getSpellSlots()
        for a, b in slots:
            self.assertEqual(a, 0)
            self.assertEqual(b, 0)        

    # django does truncation on the database level for max_length
    # so I need to enforce it in other areas I believe
    def test_truncate_name(self):
        c = Character(name='000000000100000000020000000003000000000400000000050000000006')
        with self.assertRaises(exceptions.ValidationError):
            c.full_clean()

    def test_name_on_edge(self):
        c = Character(name='00000000010000000002000000000300000000040000000005')
        c.full_clean()

        d = Character(name='000000000100000000020000000003000000000400000000051')
        with self.assertRaises(exceptions.ValidationError):
            d.full_clean()

    def test_self_truncating_name(self):
        new_name = '000000000100000000020000000003000000000400000000051'
        c = Character(name=new_name[:50])
        c.full_clean()

        new_name = 'bob'
        d = Character(name=new_name[:50])
        d.full_clean()

        self.assertEqual(new_name, d.name)

    def test_get_by_name(self):
        c = Character.objects.get(name='henry')
        self.assertNotEqual(c, None)
        self.assertEqual(c.name, 'henry')
        self.assertEqual(c.creator, 'kevin')

        with self.assertRaises(Character.DoesNotExist):
            c = Character.objects.get(name='miley')

    def test_saved_in_database(self):
        # check if all values are as expected
        c = Character.objects.get(name='Pan Bastian Edge')
        
        self.assertEqual(c.name, 'Pan Bastian Edge')
        self.assertEqual(c.creator, 'Alvin')
        
        self.assertEqual(c.char_class, 'Bard')
        self.assertEqual(c.level, 2)
        self.assertEqual(c.bg, 'Criminal/Spy')
        self.assertEqual(c.race, 'Aarakocra')
        self.assertEqual(c.alignment, 'Chaotic Neutral')
        self.assertEqual(c.exp, 10)
        self.assertEqual(c.inspiration, True)
        self.assertEqual(c.proficiency_bonus, 3)
        
        self.assertEqual(c.max_hp, 15)
        self.assertEqual(c.curr_hp, 15)
        self.assertEqual(c.temp_hp, 1)
        self.assertEqual(c.ds_success, 1)
        self.assertEqual(c.ds_failure, 1)
        
        self.assertEqual(c.ac, 12)
        self.assertEqual(c.initiative, 3)
        self.assertEqual(c.movement, 25)
        self.assertEqual(c.pass_wsd, 13)
        
        self.assertEqual(c.cp, 1)
        self.assertEqual(c.sp, 1)
        self.assertEqual(c.ep, 1)
        self.assertEqual(c.gp, 1)
        self.assertEqual(c.pp, 1)
        
        self.assertEqual(c.spell_abl, 'Charisma')
        self.assertEqual(c.spl_atk, 4)
        self.assertEqual(c.spl_save, 14)
        self.assertEqual(c.profs_lang, 'yes')
        self.assertEqual(c.feats_traits, 'no')
        self.assertEqual(c.personality, 'maybe')
        self.assertEqual(c.backstory, 'so')
        self.assertEqual(c.appearance, 'birb')

        stats = c.getStats()
        for k in stats:
            x, y, z = stats[k]
            self.assertEqual(x, 15)
            self.assertEqual(y, 1)
            self.assertEqual(z, True)

        skills = c.getSkills()
        for k in skills:
            a, b = skills[k]
            self.assertEqual(a, 1)
            self.assertEqual(b, True)

        slots = c.getSpellSlots()
        for a, b in slots:
            self.assertEqual(a, 1)
            self.assertEqual(b, 3)
        
        # check if changes save
        c.strength = 11
        c.dexterity = 13
        c.constitution = 12
        c.intelligence = 11
        c.wisdom = 16
        c.charisma = 18
        c.bg = 'Noble'
        c.gp = 15
        c.inspiration = False
        c.alignment = 'Chaotic Evil'
        c.appearance = 'Darkwing Duck *brrr brrr br brbrbrbrbrbrbrrrrrr'
        c.save()

        d = Character.objects.get(name='Pan Bastian Edge')
        self.assertEquals(c.id, d.id)
        self.assertEquals(d.name, 'Pan Bastian Edge')
        self.assertEquals(d.strength, 11)
        self.assertEquals(d.dexterity, 13)
        self.assertEquals(d.constitution, 12)
        self.assertEquals(d.intelligence, 11)
        self.assertEquals(d.wisdom, 16)
        self.assertEquals(d.charisma, 18)
        self.assertEquals(d.bg, 'Noble')
        self.assertEquals(d.gp, 15)
        self.assertEquals(d.inspiration, False)
        self.assertEquals(d.alignment, 'Chaotic Evil')
        self.assertEquals(d.appearance, 'Darkwing Duck *brrr brrr br brbrbrbrbrbrbrrrrrr')

    def test_get_same_creator(self):
        ch = list(Character.objects.filter(creator='kevin'))
        self.assertNotEqual(ch, None)
        self.assertEqual(len(ch), 2)
        self.assertNotEqual(ch[0].id, ch[1].id)

    def test_filter_startswith(self):
        ch = list(Character.objects.filter(name__startswith='P'))
        self.assertNotEqual(ch, None)
        self.assertEqual(len(ch), 2)
        self.assertNotEqual(ch[0].id, ch[1].id)

        ch2 = list(Character.objects.filter(name__startswith='Pan'))
        self.assertNotEqual(ch2, None)
        self.assertEqual(len(ch2), 1)

    def test_filter_and_order_by(self):
        ch = list(Character.objects.filter(creator='y').order_by('name'))
        self.assertEqual(len(ch), 5)
        self.assertEqual(ch[0].name, '1')
        self.assertEqual(ch[1].name, '2')
        self.assertEqual(ch[2].name, '3')
        self.assertEqual(ch[3].name, '4')
        self.assertEqual(ch[4].name, '5')

        ch2 = list(Character.objects.filter(creator='y').order_by('date'))
        self.assertEqual(len(ch2), 5)
        self.assertEqual(ch2[0].name, '1')
        self.assertEqual(ch2[1].name, '4')
        self.assertEqual(ch2[2].name, '2')
        self.assertEqual(ch2[3].name, '5')
        self.assertEqual(ch2[4].name, '3')

    def test_get_stats(self):
        a = Character.objects.get(name='henry')
        b = Character.objects.get(name='omfg')
        a_stats = a.getStats()
        b_stats = b.getStats()
        for k in a_stats:
            ax, ay, az = a_stats[k]
            bx, by, bz = b_stats[k]
            self.assertEqual(ax, 10)
            self.assertEqual(ay, 0)
            self.assertEqual(az, False)
            self.assertEqual(bx, 15)
            self.assertEqual(by, 1)
            self.assertEqual(bz, True)

    def test_get_skills(self):
        a = Character.objects.get(name='henry')
        b = Character.objects.get(name='omfg')
        a_stats = a.getSkills()
        b_stats = b.getSkills()
        for k in a_stats:
            ax, ay = a_stats[k]
            bx, by = b_stats[k]
            self.assertEqual(ax, 0)
            self.assertEqual(ay, False)
            self.assertEqual(bx, 1)
            self.assertEqual(by, True)

    def test_get_slots(self):
        a = Character.objects.get(name='henry')
        b = Character.objects.get(name='omfg')
        a_stats = a.getSpellSlots()
        b_stats = b.getSpellSlots()
        for k in range(0, len(a_stats)):
            ax, ay = a_stats[k]
            bx, by = b_stats[k]
            self.assertEqual(ax, 0)
            self.assertEqual(ay, 0)
            self.assertEqual(bx, 1)
            self.assertEqual(by, 3)
