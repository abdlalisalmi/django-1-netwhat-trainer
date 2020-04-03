from django.contrib import admin
from .models import (
        EnQuestion,
        EnChoice,
        FrQuestion,
        FrChoice
    )

# Register your models here.

class EnChoiceInline(admin.TabularInline):
    model = EnChoice
    extra = 4


class EnQuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question','id', 'correct_choice']}),
    ]
    inlines = [EnChoiceInline]
    list_display = ('question', 'id', 'date')
    list_filter = ['date']

admin.site.register(EnQuestion, EnQuestionAdmin)


class FrChoiceInline(admin.TabularInline):
    model = FrChoice
    extra = 4


class FrQuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question', 'id', 'correct_choice']}),
    ]
    inlines = [FrChoiceInline]
    list_display = ('question', 'id', 'date')
    list_filter = ['date']

admin.site.register(FrQuestion, FrQuestionAdmin)