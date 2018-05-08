import os

from collections import OrderedDict

from django.conf import settings
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
        return SubmissionChapterAuthors.objects.filter(chapter_id=chapter_id)

    def getAuthorSettings(self, author_id):
        return AuthorSettings.objects.filter(author_id=author_id)

    def getChaptersBySubmission(self, submission_id):
        return SubmissionChapters.objects.filter(submission_id=submission_id).order_by('chapter_seq')

    def getChapterSettings(self, chapter_id):
        return SubmissionChapterSettings.objects.filter(chapter_id=chapter_id, locale=locale)

    def getDigitalPublicationFormats(self, submission_id):
        return PublicationFormats.objects.filter(submission_id=submission_id, physical_format=False)

    def getChapterFileSettings(self, chapter_id):
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
        return SubmissionFiles.objects.filter(
            file_id__in=omp.getChapterFileSettings(chapter_id).values('file_id')
        ).filter(assoc_id=publication_format_id).order_by('revision').first()

    def getFileNameByFileID(self, file):
        if file:
            return '{}-{}-{}-{}-{}-{}.{}'.format(file.submission_id, file.genre_id, file.file_id, file.revision, file.file_stage, file.date_uploaded.strftime('%Y%m%d'),
             file.original_file_name.split(".")[-1])
        else: return None




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
    chapters = {}
    formats = [PublicationFormatSettings.setting_by_name.get_queryset(setting_name='name', locale=locale).filter(
        publication_format_id=pf.publication_format_id).values_list('setting_value').first()[0] for pf in
               omp.getAllPublicationFormatsBySubmission(submission_id=submission_id)]

    for chapter in omp.getChaptersBySubmission(submission_id):
        chapter_id = chapter.chapter_id
        chapters[chapter_id] = {}
        chapters[chapter.chapter_id]['settings'] = omp.getChapterSettings(chapter.chapter_id)

        chapters[chapter.chapter_id]['authors'] = [omp.getAuthor(author.author_id) for author in
                                                   omp.getAuthorsByChapter(chapter.chapter_id)]
        pfs = [omp.getFileNameByFileID(
            omp.getLatestRevisionOfChapterFileByPublicationFormat(chapter_id, int(format_id[0]))) for
               format_id in
               omp.getAllPublicationFormatsBySubmission(submission_id=submission_id).values_list(
                   'publication_format_id')]
        chapters[chapter_id]['files'] = pfs

    context = {'chapters': chapters, 'formats': formats, 'press_title': '','press_id':press_id, 'submission_id':submission_id}

    return render(request, 'workflow/index.html', context)



def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response


class PressesView(ListView):
    queryset = omp.getPresses()
    context_object_name = 'presses_list'
    template_name = "presses/index.html"
