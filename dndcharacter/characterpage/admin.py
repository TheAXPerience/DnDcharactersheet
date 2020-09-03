from django.contrib import admin
from .models import Character, Equipment, AttackSpell, CharSpells

# Register your models here.
class EquipInline(admin.TabularInline):
    model = Equipment
    extra = 0

class ASInline(admin.TabularInline):
    model = AttackSpell
    extra = 0

class CSInline(admin.TabularInline):
    model = CharSpells
    extra = 0

class CharacterAdmin(admin.ModelAdmin):
    inlines = [EquipInline, ASInline, CSInline]

admin.site.register(Character, CharacterAdmin)
