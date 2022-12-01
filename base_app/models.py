from django.db import models
from django.contrib.auth.models import User

TIPO_CLIENTE_OPCIONES = [
    ('micro', 'Micro Empresa'),
    ('pequeña', 'Empresa Pequeña'),
    ('mediana', 'Empresa Mediana'),
    ('grande', 'Empresa Grande'),
]

TIPO_SISTEMA_OPCIONES = [
    ('SAP_CRM', 'SAP CRM'),
    ('SAP_CX', 'SAP CX'),
    ('SAP_SOLMAN', 'SAP SOLMAN'),
    ('HANA', 'HANA'),
    ('CPI', 'CPI'),
    ('PO', 'PO'),
    ('PI', 'PI'),
]

TIPO_DEPARTAMENTO_OPCIONES = [
    ('solution_manager', 'Solution Manager'),
    ('CRM', 'CRM'),
    ('HANA', 'HANA'),
    ('customer_experience', 'Customer Experience'),
]

TIPO_DOCUMENTO_OPCIONES = [
    ('contrato_soporte', 'Contrato Soporte'),
    ('CRM', 'Credenciales CRM'),
    ('ERP', 'Credenciales ERP'),
    ('SOLMAN', 'Credenciales SOLMAN'),
    ('CX', 'Credenciales CX'),
    ('CPI', 'Credenciales CPI'),
    ('restricciones', 'Restricciones'),
    ('estimacion_mejora', 'Estimación de Mejora'),
    ('factibilidad_mejora', 'Factibilidad de Mejora'),
    ('presentaciones', 'Presentaciones'),
    ('otros', 'Otros'),
]

TIPO_DOCUMENTO_GENERAL_OPCIONES = [
    ('new_Release', 'New Release'),
    ('upgrade_schedule', 'Upgrade Schedule'),
    ('instructivo_integraciones', 'Instructivo Integraciones'),
    ('manual_certificaciones', 'Manual Certificaciones'),
    ('presentaciones', 'Presentaciones'),
    ('conocimiento_general', 'Conocimiento General'),
    ('otros', 'Otros'),
]


def document_upload_location(instance, filename):
    nombre_cliente = instance.cliente
    nombre_archivo = filename.lower().replace(" ", "-")
    return "client_documents/{}/{}".format(nombre_cliente, nombre_archivo)


class Consultor(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE)
    nombre = models.CharField(
        max_length=150,
        db_column='nombre',
        verbose_name='Nombre',
    )
    apellido = models.CharField(
        max_length=150,
        db_column='apellido',
        verbose_name='Apellido',
    )
    rut = models.CharField(
        max_length=20,
        db_column='rut',
        verbose_name='Rut',
        unique=True,
    )
    departamento = models.CharField(
        max_length=60,
        db_column='departamento',
        verbose_name='Departamento',
        choices=TIPO_DEPARTAMENTO_OPCIONES,
    )

    class Meta:
        db_table = 'consultor'
        verbose_name = 'Consultor'
        verbose_name_plural = 'Consultores'

    def __str__(self):
        return f"{self.usuario}"


class Cliente(models.Model):
    fecha_creacion = models.DateField(
        db_column='fecha_creacion',
        verbose_name='Fecha de creación',
        auto_now_add=True,
    )
    creado_por = models.ForeignKey(
        Consultor,
        on_delete=models.SET_NULL,
        null=True,
        db_column='creado_por',
        verbose_name='Creado Por',)
    rut = models.CharField(
        max_length=30,
        db_column='rut',
        verbose_name='Rut',
        unique=True,
    )
    nombre = models.CharField(
        max_length=200,
        db_column='nombre_contacto',
        verbose_name='Nombre Contacto',
    )
    razon_social = models.CharField(
        max_length=200,
        db_column='razon_social',
        verbose_name='Razón Social',
    )
    direccion = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        db_column='direccion',
        verbose_name='Dirección',
    )
    email = models.EmailField(
        max_length=100,
        db_column='email',
        verbose_name='Email',
    )
    telefono = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        db_column='telefono',
        verbose_name='Teléfono',
    )
    tipo_cliente = models.CharField(
        max_length=50,
        db_column='tipo_cliente',
        verbose_name='Tipo de Cliente',
        choices=TIPO_CLIENTE_OPCIONES,
    )
    tipo_sistema = models.CharField(
        max_length=50,
        db_column='tipo_sistema',
        verbose_name='Tipo de sistemas',
        choices=TIPO_SISTEMA_OPCIONES,
    )

    def __str__(self):
        return f"{self.rut} - {self.nombre}"

    class Meta:
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class DocumentoCliente(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE
    )
    nombre_documento = models.CharField(
        max_length=150,
        db_column='nombre_documento',
        verbose_name='Nombre Documento',
    )
    descripcion_documento = models.TextField(
        blank=True,
        null=True,
        default=None,
        db_column='descripcion_documento',
        verbose_name='Descripción del Documento',
    )
    tipo_documento = models.CharField(
        max_length=100,
        db_column='tipo_documento',
        verbose_name='Tipo de Documento',
        choices=TIPO_DOCUMENTO_OPCIONES,
    )
    documento = models.FileField(
        upload_to=document_upload_location,
        verbose_name='Documento',
        blank=True,
        null=True,
    )

    class Meta:
        db_table = 'documentos_clientes'
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'


class RecomendacionCliente(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE
    )
    recomendacion = models.TextField(
        db_column='recomendacion',
        verbose_name='Recomendación',
    )

    class Meta:
        db_table = 'recomendacion'
        verbose_name = 'Recomendacion'
        verbose_name_plural = 'Recomendaciones'


class DocumentoGeneral(models.Model):

    nombre = models.CharField(
        max_length=150,
        db_column='nombre_documento_general',
        verbose_name='Nombre Documento',
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
        db_column='descripcion_doc',
        verbose_name='Descripción del Documento',
    )
    tipo = models.CharField(
        max_length=150,
        db_column='tipo_doc_general',
        verbose_name='Tipo de Documento',
        choices=TIPO_DOCUMENTO_GENERAL_OPCIONES,
    )

    documento = models.FileField(
        upload_to='general_documents/',
        verbose_name='Documento',
    )

    class Meta:
        db_table = 'documento_general'
        verbose_name = 'Documento General'
        verbose_name_plural = 'Documentos Generales'
