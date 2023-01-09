from django.contrib import admin
from base_app.models import (
    Cliente,
    Consultor,
    DocumentoCliente,
    DocumentoGeneral,
    RecomendacionCliente)


class DocumentoInLine(admin.StackedInline):
    model = DocumentoCliente
    extra = 1


class RecomendacionInLine(admin.StackedInline):
    model = RecomendacionCliente
    extra = 1


class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'rut',
        'fecha_creacion',
        'creado_por',
        'nombre',
        'razon_social',
        'direccion',
        'email',
        'telefono',
        'tipo_cliente',
        'tipo_sistema',
    )
    inlines = [DocumentoInLine, RecomendacionInLine]

    readonly_fields = (
        'creado_por',
    )

    def save_model(self, request, obj, form, change):
        if not change:
            consultor = Consultor.objects.get(id=request.user.id)
            print(consultor)
            obj.creado_por = consultor
        super().save_model(request, obj, form, change)


class ConsultorAdmin(admin.ModelAdmin):
    list_display = (
        'usuario',
        'nombre',
        'apellido',
        'rut',
        'departamento',
    )


class DocumentoClienteAdmin(admin.ModelAdmin):
    list_display = (
        'cliente',
        'nombre_documento',
        'descripcion_documento',
        'tipo_documento',
        'documento',
    )


class DocumentosGeneralesAdmin(admin.ModelAdmin):
    list_display = (
        'creado_por',
        'nombre',
        'descripcion',
        'tipo',
        'documento',
    )

    readonly_fields = (
        'creado_por',
    )

    def save_model(self, request, obj, form, change):
        if not change:
            consultor = Consultor.objects.get(id=request.user.id)
            print(consultor)
            obj.creado_por = consultor
        super().save_model(request, obj, form, change)


class RecomendacionAdmin(admin.ModelAdmin):
    list_display = (
        'cliente',
        'recomendacion',
    )


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Consultor, ConsultorAdmin)
admin.site.register(DocumentoCliente, DocumentoClienteAdmin)
admin.site.register(DocumentoGeneral, DocumentosGeneralesAdmin)
admin.site.register(RecomendacionCliente, RecomendacionAdmin)
