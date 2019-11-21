from django.contrib import admin
from .models import MedicalDepartment, SelfDiagnosis, Symtom, Treatment, Disease

admin.site.register(MedicalDepartment)
admin.site.register(Treatment)
admin.site.register(Disease)
admin.site.register(Symtom)
admin.site.register(SelfDiagnosis)




