from django.shortcuts import render
from .services import get_music

def search(request):
    query = request.GET.get('q')
    songs = []
    if query:
        data = get_music(query)
        if data:
                songs = data.get('data', [])
    return render(request, 'music.html', {'songs': songs, 'query': query})