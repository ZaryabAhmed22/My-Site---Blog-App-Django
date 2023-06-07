from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="index"),
    path("posts/", views.AllPostView.as_view(), name="posts"),
    path("posts/<slug:slug>",
         views.PostDetailView.as_view(), name="post-detail"),
    path("read-later", views.ReadLaterView, name="read-later")
]
