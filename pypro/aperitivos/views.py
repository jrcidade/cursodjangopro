from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 681146135},
        'instalacao-windows': {'titulo': 'Instalação do Windows', 'vimeo_id': 681146168},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
