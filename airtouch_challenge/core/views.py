from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import NutritionalInformation, Product
from .forms import NutritionalInformationForm, ProductForm


# Nutritional Information Views.
@login_required
def ni_list(request):
    items = NutritionalInformation.objects.all().order_by("name")
    return render(request, "core/ni_list.html", {"items": items})


@login_required
def ni_detail(request, pk):
    obj = get_object_or_404(NutritionalInformation, pk=pk)
    return render(request, "core/ni_detail.html", {"obj": obj})


@login_required
def ni_create(request):
    form = NutritionalInformationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Nutritional information created.")
        return redirect("ni_list")
    return render(request, "core/ni_form.html", {"form": form})


@login_required
def ni_update(request, pk):
    obj = get_object_or_404(NutritionalInformation, pk=pk)
    form = NutritionalInformationForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Nutritional information updated.")
        return redirect("ni_detail", pk=obj.pk)
    return render(request, "core/ni_form.html", {"form": form, "obj": obj})


@login_required
def ni_delete(request, pk):
    obj = get_object_or_404(NutritionalInformation, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Nutritional information deleted.")
        return redirect("ni_list")
    return render(request, "core/confirm_delete.html", {"obj": obj, "type": "Nutritional Information"})


@login_required
def ni_list(request):
    items = NutritionalInformation.objects.all().order_by("name")
    return render(request, "core/ni_list.html", {"items": items})


@login_required
def ni_detail(request, pk):
    obj = get_object_or_404(NutritionalInformation, pk=pk)
    return render(request, "core/ni_detail.html", {"obj": obj})


@login_required
def ni_create(request):
    form = NutritionalInformationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Información nutricional creada.")
        return redirect("ni_list")
    return render(request, "core/ni_form.html", {"form": form})


@login_required
def ni_update(request, pk):
    obj = get_object_or_404(NutritionalInformation, pk=pk)
    form = NutritionalInformationForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Información nutricional actualizada.")
        return redirect("ni_detail", pk=obj.pk)
    return render(request, "core/ni_form.html", {"form": form, "obj": obj})


@login_required
def ni_delete(request, pk):
    obj = get_object_or_404(NutritionalInformation, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Información nutricional eliminada.")
        return redirect("ni_list")
    return render(request, "core/confirm_delete.html", {"obj": obj, "type": "Nutritional Information"})


# Product Views.
@login_required
def product_list(request):
    products = Product.objects.all().order_by("name")
    return render(request, "core/product_list.html", {"products": products})


@login_required
def product_detail(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    return render(request, "core/product_detail.html", {"obj": obj})


@login_required
def product_create(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Producto creado.")
        return redirect("product_list")
    return render(request, "core/product_form.html", {"form": form})


@login_required
def product_update(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Producto actualizado.")
        return redirect("product_detail", pk=obj.pk)
    return render(request, "core/product_form.html", {"form": form, "obj": obj})


@login_required
def product_delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Producto eliminado.")
        return redirect("product_list")
    return render(request, "core/confirm_delete.html", {"obj": obj, "type": "Product"})
