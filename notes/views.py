from django.shortcuts import render,redirect
from .forms import NoteForm
from .models import Note
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    notes = Note.objects.filter(user=request.user)

    query = request.GET.get('search')

    if query:
        notes = notes.filter(title__icontains = query) | notes.filter(content__icontains=query)
    
    paginator = Paginator(notes, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_notes = notes.count()

    context = {
        'notes':page_obj,
        'total_notes':total_notes,
    }    

    return render(request, 'notes/dashboard.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form':form}) 


@login_required(login_url='login')
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, "Note Created Successfully")
            return redirect('dashboard')
    else:
        form = NoteForm

    return render(request, 'notes/add_note.html', {'form':form})    


@login_required(login_url='login')
def note_detail(request, id):

    note = Note.objects.get(id = id, user=request.user)

    return render(request, 'notes/note_detail.html', {'note':note})



@login_required(login_url='login')
def edit_note(request, id):

    note = Note.objects.get(id=id, user=request.user)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            messages.success(request, "Note updated successfully!")

            return redirect('dashboard')
        
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/edit_note.html', {'form':form}) 


@login_required(login_url='login')
def delete_note(request, id):

    note = Note.objects.get(id=id, user=request.user)

    if request.method == 'POST':

        note.delete()
        messages.success(request, "Note Deleted successfully!")

        return redirect('dashboard')
    
    return render(request, 'notes/delete_note.html', {'note':note})


@login_required(login_url='login')
def profile(request):

    user = request.user
    return render(request, 'notes/profile.html', {'user':user})


