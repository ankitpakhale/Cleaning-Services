from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from FBV.models import Book
from .forms import BookForm


def book_list(request, template_name='FBV/book_list.html'):
    book = Book.objects.all()
    return render(request, template_name, {'object_list':book})

def book_view(request, pk, template_name='FBV/book_detail.html'):
    book= get_object_or_404(Book, pk=pk)    
    return render(request, template_name, {'object':book})

def book_create(request, template_name='FBV/book_form.html'):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form':form})

def book_update(request, pk, template_name='FBV/book_form.html'):
    book= get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form':form})

def book_delete(request, pk, template_name='FBV/book_confirm_delete.html'):
    book= get_object_or_404(Book, pk=pk)   
    book.delete() 
   # if request.method=='POST':
     #   book.delete()
    return redirect('book_list')
   # return render(request, template_name, {'object':book})