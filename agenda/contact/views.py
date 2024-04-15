from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

def contact_index(request,letter=None):

    if letter:
        contacts = Contact.objects.filter(name__istartswith=letter)
    else:
        contacts = Contact.objects.filter(name__contains=request.GET.get('search','').strip().capitalize())

    context = {'contacts':contacts}

    return render(request, 'contact/index.html',context)


def contact_view(request,id):

    contact = Contact.objects.get(id=id)
    context = {'contact': contact}

    return render(request, 'contact/contact_view.html', context)


def update_contact(request,id):
    contact = Contact.objects.get(id = id)

    if request.method == 'GET':
        form = ContactForm(instance=contact)
        context = {'form': form, 'id':id}

        return render(request, 'contact/contact_form.html', context)

    if request.method == 'POST':
        user_updated = ContactForm(request.POST, instance = contact)

        if user_updated.is_valid():
            user_updated.save()
        context = {'form': user_updated,'id':id}

        message = 'Contact Updated'
        messages.success(request, message)

        return render(request, 'contact/contact_form.html', context)


def create_contact(request):

    if request.method == 'GET':
        form = ContactForm()
        context = {'form':form}

        return render(request, 'contact/contact_form.html',context)
    
    if request.method == 'POST':
        new_user = ContactForm(request.POST)

        if new_user.is_valid():
            new_user.save()
        context = {'form':new_user}

        return redirect('contact_index')


def delete_contact(request,id):

    contact = Contact.objects.get(id=id).delete()

    return redirect('contact_index')

