from django.shortcuts import render, redirect

# Create your views here.
from .forms import ModelDataForm
from django.http import HttpResponseRedirect, Http404

# Create your views here.

def home_view(request):
    template = 'home.html'
    if request.method == 'GET':
        context = {'form': ModelDataForm()}
        return render(request, template, context)
    if request.method == 'POST':
        form = ModelDataForm(request.POST)
        if form.is_valid():
            shortener =  form.save()
            old_url = shortener.old_url
            new_url = request.build_absolute_uri('/') + shortener.short_url
            context = {'old_url': old_url, 'new_url': new_url}
            return render(request, template, context)
    context = {'errors': form.errors}
    return render(request, template, context)


def redirect_view(request, shortened):
    try:
        data = ModelData.objects.get(short_url=shortened)
        data.save()
        return HttpResponseRedirect(data.url)
    except:
        raise Http404('Sorry, the link is not valid')

