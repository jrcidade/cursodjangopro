from django.shortcuts import render

videos = [
    {'slug': 'motivacao', 'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 681146135},
    {'slug': 'instalacao-windows', 'titulo': 'Instalação do Windows', 'vimeo_id': 681146168},
]

videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
