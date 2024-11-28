from django.shortcuts import render


def index_view(request):
    ctx = {
        'a': 'b',
    }
    return render(request, template_name='index.html', context=ctx)
