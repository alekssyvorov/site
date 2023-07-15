from django.contrib import admin

from .models import Products, Register


class RegisterAdmin(admin.ModelAdmin):
    list_display = ("name", "password", "email")


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price")


# Register your models here.
admin.site.register(Register, RegisterAdmin)
admin.site.register(Products, ProductsAdmin)
