from django.contrib import admin
from .models import *


# Register your models here.
# admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Course)

#Варіант реєстрації Company, якщо плануються налаштовування відображення в адмінці,
# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return not Company.objects.exists()

#Варіант реєстрації Student, якщо плануються налаштовування відображення в адмінці,
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    form = StudentAdminForm
