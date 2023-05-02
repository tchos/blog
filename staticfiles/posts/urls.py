from django.urls import path

from .views import BlogHome, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete

# posts represente le nom de notre application, il nous seras important pour identifier de manière unique une url
app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('create/', BlogPostCreate.as_view(), name="create"),
    path('edit/<str:slug>/', BlogPostUpdate.as_view(), name="edit"),
    path('<str:slug>/', BlogPostDetail.as_view(), name="post"),
    path('delete/<str:slug>/', BlogPostDelete.as_view(), name="delete"),
]