from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import BlogPost

# Create your views here.
#Liste des posts
class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"
    template_name = "posts/posts_list.html"

    """Affichier seulement les posts publiés si aucun user connecté
        La fonction doit obligatoirement s'appeler get_queryset
    """
    def get_queryset(self):
        # le queryset contient tous les articles créés.
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        # Si user pas connecté, on n'affiche que les posts publiés.
        return queryset.filter(published=True)

#Création d'un post, pour le faire il faut être connecté
@method_decorator(login_required, name='dispatch')
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/posts_create.html"
    # Liste des champs à afficher dans le formulaire e création d'un nouveau posts
    fields = ['title', 'content', ]
    # redirection en cas de céation d'un article avec succès
    success_url = reverse_lazy("posts:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Créer"
        return context

# Modification d'un article
class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/posts_edit.html"
    # Liste des champs à afficher dans le formulaire e création d'un nouveau posts
    fields = ['title', 'content', 'published', ]
    # redirection en cas de céation d'un article avec succès
    success_url = reverse_lazy("posts:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Editer"
        return context

# Afficher les détails sur un article
class BlogPostDetail(DetailView):
    model = BlogPost
    template_name = "posts/post_detail.html"
    context_object_name = "article"

# Supprimer un article
class BlogPostDelete(DeleteView):
    model = BlogPost
    template_name = "posts/post_delete_confirm.html"
    context_object_name = "article"
    success_url = reverse_lazy("posts:home")