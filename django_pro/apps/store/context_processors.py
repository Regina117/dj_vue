from .models import Category

def menu_categories(requst):
    categories=Category.objects.all()
    
    return {'menu_categories': categories}