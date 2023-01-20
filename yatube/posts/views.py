from django.http import HttpResponse

def index(request):
    return HttpResponse('Главноая страница')

def group_posts(request, post):
    return HttpResponse(f'Группа {post}')