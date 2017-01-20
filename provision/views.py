from django.shortcuts import render
from .models import Box
from .forms import AddBoxForm
from django.http import HttpResponseRedirect

def IndexView(request):
    """
    Index page for provision
    """
    box_list = Box.objects.all()
    context = {'box_list': box_list}
    return render(request, 'provision/index.html', context)

def AddBoxView(request):
    """
    Adding Box form
    """
    if request.method == 'GET':
        box_add_form = AddBoxForm()
    else:
        box_add_form = AddBoxForm(request.POST)
        if box_add_form.is_valid():
            box_name = box_add_form.cleaned_data['box_name']
            box_author = box_add_form.cleaned_data['box_author']
            box_url = box_add_form.cleaned_data['box_url']
            box_os = box_add_form.cleaned_data['box_os']
            box_checksum = box_add_form.cleaned_data['box_checksum']
            box_builders = box_add_form.cleaned_data['box_builders']

            post = Box.objects.create(box_name=box_name,
                                      box_author=box_author,
                                      box_url=box_url,
                                      box_os=box_os,
                                      box_checksum=box_checksum,
                                      box_builders=box_builders)
            return HttpResponseRedirect('/provision/box_details')
    return render(request, 'provision/form_box_add.html', {'form':box_add_form})
