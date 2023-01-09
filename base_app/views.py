from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Exitoso.")
            return redirect("/admin")
        messages.error(
            request, "Ha fallado el registro. Información inválida.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def admin_view(request):
    return redirect("admin/")
