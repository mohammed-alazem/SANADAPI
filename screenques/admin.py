from django.contrib import admin
from django.utils.html import format_html
from .models import TempList


# Register your models here.

class TempListAdmin(admin.ModelAdmin):
    list_display = ("Name", "Answer", "sub", "del_temp")

    def sub(self, obj):
        return format_html(
            '<form action="/inter_action_question_move/?id=%s" method="post"><button class="button" value="submit">'
            'Accept</button></form>' % obj.id)

    def del_temp(self, obj):
        return format_html(
            '<form action="/inter_action_question_delete/?id=%s" method="post"><button class="button" value="delete">'
            'Decline</button></form>' % obj.id)

    sub.short_description = 'SendToScreen'
    del_temp.short_description = 'delete'


admin.site.register(TempList, TempListAdmin)
