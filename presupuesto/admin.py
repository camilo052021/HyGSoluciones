from django.contrib import admin
from presupuesto.models import *

# Register your models here.

class PeriodoAdmin(admin.ModelAdmin):
    readonly_fields = ['create_at', 'modify_at']
    list_display = ['anio']   
    search_fields = ['anio']    
    list_filter = ['anio']

    class Meta:
        models = 'Periodo'
admin.site.register(Periodo,PeriodoAdmin)



class EjecucionPresupuestoAdmin(admin.ModelAdmin):
    readonly_fields = ['create_at', 'modify_at']
    list_display = ['id_proveedor']   
    search_fields = ['id_proveedor']    
    list_filter = ['id_proveedor']

    class Meta:
        models = 'Ejecución'
admin.site.register(EjecucionPresupuesto,EjecucionPresupuestoAdmin)


admin.site.register(CronogramaPresupuesto)