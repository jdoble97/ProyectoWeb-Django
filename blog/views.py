from django.shortcuts import render
from .models import Post, Categoria
# Create your views here.
def blog(req):
    posts = Post.objects.all()
    return render(req, 'blog/blog.html',{'posts':posts})

def categoria(req, categoria_id):
    ctgoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias = ctgoria)
    return render(req, 'blog/categoria.html', {'categoria': categoria, 'posts':posts})