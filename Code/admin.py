from django.contrib import admin
from .models import Category,Problem,ForeignResource,LanguageCategory,SolutionCode,CommentData,Dates,ResourceTag
from django.contrib.auth.models import User,Group
# Register your models here.

class InlineForeignResource(admin.TabularInline):
    model = ForeignResource
    extra = 3

class InlineSolutionCode(admin.TabularInline):
    model = SolutionCode
    extra = 1

class ProblemAdmin(admin.ModelAdmin):
    inlines = [InlineForeignResource,InlineSolutionCode]

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Problem,ProblemAdmin)
admin.site.register(Category)
admin.site.register(CommentData)
admin.site.register(LanguageCategory)
admin.site.register(Dates)
admin.site.register(ResourceTag)