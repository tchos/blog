from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.db import models

# Recupération du user connecté
User = get_user_model()

# Create your models here.
class BlogPost(models.Model):
    # unique=True => il ne doit pas 2 articles avec le même titre en BD
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    # unique=True => il ne doit pas 2 articles avec le même slug en BD
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # La date du jour de modification sera automatiquement la date de dernière mise à jour
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")

    class Meta:
        # Classement par la date de création des article odre décroissant dans le panel d'administration
        ordering=['-created_on']
        # Affichera 'Articles' au lieu de 'BlogPost' dans le panel d'administration
        verbose_name='Article'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # si le slug n'est pas défini, on le calcul automatiquement
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    @@property
    def author_or_default(self):
        # Condition ternaire
        return self.author.username if self.author else "Un auteur inconnu"

        """Le code ci-dessus est équivalent au code ci-dessous
        if self.author:
            return self.author.username
        return "Un auteur inconnu"
        """


