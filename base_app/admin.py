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
        'fecha_creacion',
        'creado_por',
        'rut',
        'nombre',
        'razon_social',
        'direccion',
        'email',
        'telefono',
        'tipo_cliente',
        'tipo_sistema',
    )
    inlines = [DocumentoInLine, RecomendacionInLine]


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
        'nombre',
        'descripcion',
        'tipo',
        'documento',
    )


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
