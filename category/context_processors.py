from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)


def context(request):
    context = {
    'CANONICAL_PATH': request.build_absolute_uri(request.path),
    }
    return context
