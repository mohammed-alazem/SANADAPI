from django.contrib import admin
from .models import Teams, AudienceAward, JudgingMarks


class TeamsAdmin(admin.ModelAdmin):
    list_display = ("TeamNumber", "Name")
    list_filter = ("TeamNumber", "Name")


class AudienceAwardAdmin(admin.ModelAdmin):
    list_display = ("TeamNumber", "Name", "ID_Audience")
    list_filter = ("TeamNumber", "Name", "ID_Audience")


class JudgingMarksAdmin(admin.ModelAdmin):
    list_display = ("TeamNumber", "JudgType", "MarkAndQuestions")
    list_filter = ("TeamNumber", "JudgType", "MarkAndQuestions")


admin.site.register(Teams, TeamsAdmin)
admin.site.register(JudgingMarks, JudgingMarksAdmin)
admin.site.register(AudienceAward, AudienceAwardAdmin)
