# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.contrib import admin
from models import Tag, Contact


# Register your models here.
class TagInLine(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    # fields = ('name', 'email')
    list_display = ('name','age', 'email') # list
    inlines = [TagInLine]  # inline
    search_fields = ('name',)
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Tag])
# admin.site.register([Contact, Tag])
