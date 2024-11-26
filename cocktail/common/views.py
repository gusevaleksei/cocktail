from django.http import JsonResponse


def version(request):
    d = {
        'a': 'b',
        # 'source': settings.SOURCE,
        # 'version': settings.VERSION,
        # 'commit': settings.GIT_COMMIT,
        # 'build': settings.PIPELINE_ID,
    }
    return JsonResponse(d)
