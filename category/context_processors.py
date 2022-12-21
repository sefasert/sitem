from .models import Category, Setting

def menu_links(request):
    links = Category.objects.all()
    ayarlar = Setting.objects.all()
    return dict(links=links, ayarlar=ayarlar)


def context(request):
    context = {
    'CANONICAL_PATH': request.build_absolute_uri(request.path),
    }
    return context
