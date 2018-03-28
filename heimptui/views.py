import  numpy as np
from collections import OrderedDict

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import *

locale = 'de_DE'


class OMPDAL:
    def __init__(self):
        pass

    def getAllPublicationFormatsBySubmission(self, submission_id):
        return PublicationFormats.objects.filter(submission_id=submission_id)

    def getAuthor(self, author_id):
        return Authors.objects.filter(author_id=author_id)

    def getAuthorsByChapter(self, chapter_id):
        return SubmissionChapterAuthors.objects.filter(chapter_id= chapter_id)

    def getAuthorSettings(self, author_id):
        return AuthorSettings.objects.filter(author_id=author_id)

    def getChaptersBySubmission(self, submission_id):
        return SubmissionChapters.objects.filter(submission_id=submission_id).order_by('chapter_seq')

    def getChapterSettings(self, chapter_id):
        return SubmissionChapterSettings.objects.filter(chapter_id=chapter_id)

    def getDigitalPublicationFormats(self, submission_id):
        return PublicationFormats.objects.filter(submission_id=submission_id, physical_format=False)

    def getChapterFile(self, chapter_id):
        return SubmissionFileSettings.objects.filter(setting_name='chapterID').filter(setting_value=chapter_id)

    def getPhysicalPublicationFormats(self, submission_id):
        return PublicationFormats.objects.filter(submission_id=submission_id, physical_format=True)

    def getPresses(self):
        return Presses.objects.order_by('path')

    def getPressSettings(self, press_id):
        return PressSettings.objects.filter(press_id=press_id)

    def getPublicationFormatsBySubmission(self, submission_id):
        return PublicationFormats.objects.filter(submission_id=submission_id)

    def getPublicationFormatSettings(self, publication_format_id):
        return PublicationFormatSettings.objects.filter(publication_format_id=publication_format_id)

    def getSubmissionsByPress(self, press_id, status):
        return Submissions.objects.filter(context_id=press_id, status=status)

    def getSubmissionSettings(self, submission_id):
        return SubmissionSettings.objects.filter(submission_id=submission_id)

    def getStageAssignments(self, submission_id):
        return StageAssignments.objects.filter(submission_id=submission_id)

    def getUserSettings(self, user_id):
        return Users.objects.filter(user_id=user_id)

    def getLatestRevisionOfChapterFileByPublicationFormat(self, chapter_id, publication_format_id):
        return SubmissionFiles.objects.filter(file_id__in=SubmissionFileSettings.objects.filter(setting_name="chapterID", setting_value=chapter_id),assoc_id=publication_format_id, file_stage=10)


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
        title = SubmissionSettings.setting_by_name.get_queryset(setting_name='title', locale=locale).filter(
            submission_id=s.submission_id).values('setting_value').first()
        sl[s.submission_id]['title'] = title['setting_value'] if title else ''
    stage_assignments = {}
    for s in submissions_list:
        stage_assignments[s.submission_id] = \
        omp.getStageAssignments(s.submission_id).order_by('-date_assigned').values('user_id').first()['user_id']

    for s in stage_assignments:
        u = Users.objects.filter(user_id=stage_assignments[s]).values('initials')
        sl[s]['initials'] = u.first()['initials'] if u else ''

    context = {
        'sl': sl,
        'press_title': PressSettings.setting_by_name.get_queryset(setting_name='name', locale=locale).filter(
            press_id=press_id),
        'press_id': press_id
    }

    return render(request, 'submissions/index.html', context)


def workflow(request, press_id, submission_id, stage_id):
    chapters ={}
    pfs = [x for x in omp.getAllPublicationFormatsBySubmission(submission_id=submission_id).values_list('publication_format_id')]
    formats = [PublicationFormatSettings.setting_by_name.get_queryset(setting_name='name', locale=locale).filter(publication_format_id=x[0]).values_list('setting_value').first()[0] for x in pfs]
    for chapter in  omp.getChaptersBySubmission(submission_id):
        chapters[chapter.chapter_id] = {}
        #chapters[chapter.chapter_id]['settings'] = omp.getChapterSettings(chapter.chapter_id)
        #chapters[chapter.chapter_id]['authors'] = omp.getAuthorsByChapter(chapter.chapter_id)
        chapters[chapter.chapter_id]['files'] = omp.getLatestRevisionOfChapterFileByPublicationFormat(chapter.chapter_id,149)
        chapters[chapter.chapter_id]['formats'] = pfs



    context = {'chapters': chapters, 'press_title': ''}

    return render(request, 'workflow/index.html', context)


class PressesView(ListView):
    queryset = omp.getPresses()
    context_object_name = 'presses_list'
    template_name = "presses/index.html"
