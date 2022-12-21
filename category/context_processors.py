from .models import Category, Setting

def menu_links(request):
    links = Category.objects.all()
    setting = Setting.objects.all()
    return dict(links=links, setting=setting)


def context(request):
    context = {
    'CANONICAL_PATH': request.build_absolute_uri(request.path),
    }
    return context
