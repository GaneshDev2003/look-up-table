from django.shortcuts import render

# Create your views here.
from .models import EntriesModel
from .forms import EntryForm
def entry_create_view(request):
    form = EntryForm(request.POST or None)
    if(form.is_valid()):
        form.save();
    return render(request,'entry_create.html',{'form':form})

