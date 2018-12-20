from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from pharmacy.forms import UserForm, PharmacyForm, UserFormForEdit, DrugForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from pharmacy.models import Drug

# Create your views here.
def home(request):
    return redirect(pharmacy_home)

@login_required(login_url='/pharmacy/sign-in/')
def pharmacy_home(request):
    return redirect(pharmacy_home)

@login_required(login_url='/pharmacy/sign-in/')
def pharmacy_account(request):
    user_form = UserFormForEdit(instance=request.user)
    pharmacy_form = PharmacyForm(instance=request.user.pharmacy)

    if request.method == 'POST':
        user_form = UserFormForEdit(request.POST, instance=request.user)
        pharmacy_form = PharmacyForm(request.POST, request.FILES, instance=request.user.pharmacy)

        if user_form.is_valid() and pharmacy_form.is_valid():
            user_form.save()
            pharmacy_form.save()

    return render(request, 'pharmacy/account.html', {
        'user_form' : user_form,
        'pharmacy_form' : pharmacy_form
    })

@login_required(login_url='/pharmacy/sign-in/')
def pharmacy_drug(request):
    drugs = Drug.objects.filter(pharmacy=request.user.pharmacy).order_by("-id")
    return render(request, 'pharmacy/drug.html', {
        'drugs': drugs
    })

@login_required(login_url='/pharmacy/sign-in/')
def pharmacy_add_drug(request):
    form = DrugForm()

    if request.method == "POST":
        form = DrugForm(request.POST, request.FILES)
        if form.is_valid():
            drug = form.save(commit=False)
            drug.pharmacy = request.user.pharmacy
            drug.save()
            return redirect(pharmacy_drug)
            
    return render(request, 'pharmacy/add_drug.html', {
        'form': form
    })

@login_required(login_url='/pharmacy/sign-in/')
def pharmacy_edit_drug(request, drug_id):
    form = DrugForm(instance=Drug.objects.get(id=drug_id))

    if request.method == "POST":
        form = DrugForm(request.POST, request.FILES, instance=Drug.objects.get(id=drug_id))
        if form.is_valid():
            drug = form.save()
            return redirect(pharmacy_drug)
            
    return render(request, 'pharmacy/edit_drug.html', {
        'form': form
    })


def pharmacy_sign_up(request):
    user_form = UserForm
    pharmacy_form = PharmacyForm
    
    if request.method == "POST":
        user_form = UserForm(request.POST)
        pharmacy_form = PharmacyForm(request.POST, request.FILES)

        if user_form.is_valid() and pharmacy_form.is_valid:
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_pharmacy = pharmacy_form.save(commit=False)
            new_pharmacy.owner = new_user
            new_pharmacy.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            ))

            return redirect(pharmacy_home)


    return render(request, 'pharmacy/sign_up.html', {
        'user_form' : user_form,
        'pharmacy_form' : pharmacy_form
    })

