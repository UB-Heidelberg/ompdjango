from collections import OrderedDict

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Presses, PressSettings, StageAssignments, Submissions, SubmissionSettings, Users

locale = 'de_DE'


class OMPDAL:
    def __init__(self):
        pass

    def getPresses(self):
        return Presses.objects.order_by('path')

    def getPressSettings(self, press_id):
        return PressSettings.objects.filter(press_id=press_id)

    def getSubmissionsByPress(self, press_id, status):
        return Submissions.objects.filter(context_id=press_id, status=status)

    def getSubmissionSettings(self, submission_id):
        return SubmissionSettings.objects.filter(submission_id=submission_id)

    def getStageAssignments(self, submission_id):
        return StageAssignments.objects.filter(submission_id=submission_id)

    def getUserSettings(self,user_id):
        return Users.objects.filter(user_id=user_id)

    def getPressSettingsName(self, press_id, name):
        return self.getPressSettings(press_id).filter(setting_name=name, locale=locale).values('setting_value')

    def getSubmissionSettingsByType(self, submission_id, type):
        try:
            return omp.getSubmissionSettings(submission_id).filter(setting_name=type, locale=locale).values('setting_value')[0]['setting_value']
        except:
            return ''

    def getUserSettingsByType(self, stage_assignments, type):
        try:
            return omp.getUserSettings(stage_assignments).values(type)[0][type]
        except:
            return ''



omp = OMPDAL()


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, submission_id):
    submissions_list = Submissions.objects.order_by('-last_modified')[:10]

    context = {
        'submissions_list': submissions_list
    }

    return render(request, 'press/index.html', context)


def submissions(request, press_id):
    submissions_list = omp.getSubmissionsByPress(press_id, 1).order_by('last_modified')


    sl = OrderedDict()
    for s in submissions_list:
        sl[s.submission_id] = {'id': s.submission_id}
        sl[s.submission_id]['title'] = omp.getSubmissionSettingsByType(s.submission_id, 'title')

    stage_assignments = {}
    for s in submissions_list:
        try:
            stage_assignments[s.submission_id] = omp.getStageAssignments(s.submission_id).order_by('-date_assigned')[
                0].user_id
        except:
            pass

    for sa in stage_assignments:
        sl[sa]['initials'] = omp.getUserSettingsByType(stage_assignments[sa], 'initials')

    context = {
        'sl': sl,
        'press_title': omp.getPressSettingsName(press_id, 'title'),
        'press_id': press_id
    }

    return render(request, 'submissions/index.html', context)





def workflow(request, press_id, submission_id, stage_id):
    sl = ''
    context = {'sl': sl, 'press_title': ''}

    return render(request, 'workflow/index.html', context)


class PressesView(ListView):
    queryset = omp.getPresses()
    context_object_name = 'presses_list'
    template_name = "presses/index.html"
