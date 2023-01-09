from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission, Group
from base_app.models import Consultor


# Create your forms here.

TIPO_DEPARTAMENTO_OPCIONES = [
    ('solution_manager', 'Solution Manager'),
    ('CRM', 'CRM'),
    ('HANA', 'HANA'),
    ('customer_experience', 'Customer Experience'),
]


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    rut = forms.CharField(required=True)
    departamento = forms.ChoiceField(
        required=True, choices=TIPO_DEPARTAMENTO_OPCIONES)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'rut', 'departamento', 'email',)

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellido"

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.rut = self.cleaned_data['rut']
        user.departamento = self.cleaned_data['departamento']
        user.is_staff = True

        if commit:
            user.save()
            consultor = Consultor.objects.create(
                usuario_id=user.id, nombre=user.first_name,
                apellido=user.last_name, rut=user.rut,
                departamento=user.departamento
            )
            consultor_group = Group.objects.get(name='Consultores')
            user.groups.set([consultor_group,])

            return user
