from django.shortcuts import render

from blog.models import Post, Categoria

# Create your views here.

def blog(request):
    """A view that shows all blog"""
    post = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": post})

def categoria(request, categoria_id):
    """A view that shows category filter by id."""
    categoria = Categoria.objects.get(id=categoria_id)
    post = Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {'categoria': categoria,'posts': post})
