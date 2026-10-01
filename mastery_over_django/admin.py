from django.contrib import admin
from .models import Mastery,Comment

class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 1

class MasteryAdmin(admin.ModelAdmin):
    fieldSets = [
        ('Informações', {'fields': ['mastery_name','mastery_description']}),
        ('Data', {'fields': ['pub_date']})
        
        ]
    inlines = [CommentInLine]


admin.site.register(Mastery, MasteryAdmin)