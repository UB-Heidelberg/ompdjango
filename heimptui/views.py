from django.http import HttpResponse
from django.shortcuts import render
from .models import Submissions


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, submission_id):
    submissions_list = Submissions.objects.order_by('-last_modified')[:10]

    context = {
        'submissions_list': submissions_list
    }

    return render(request, 'detail/index.html', context)
