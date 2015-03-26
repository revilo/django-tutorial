from django.contrib import admin
from polls.models import Choice, Poll

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date')
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)   # make Polls editable in admin site
