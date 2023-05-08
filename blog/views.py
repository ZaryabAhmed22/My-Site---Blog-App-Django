from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Zaryab Ahmed",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothin like the views you get when hiking in the mountains! And I was't even prepared for what happened whilst I was enjoying the view!",
        "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut volutpat velit. Morbi luctus ultrices sodales. Integer pulvinar ligula et erat ultrices, non placerat eros condimentum. Proin sagittis interdum justo, sit amet lacinia odio consequat sed. Aenean malesuada libero vitae efficitur tristique. Etiam dictum laoreet lorem, id faucibus felis bibendum id. Aenean tincidunt eros sem, nec vulputate eros porttitor fringilla. Phasellus justo mauris, porttitor in metus eget, hendrerit aliquam justo.

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut volutpat velit. Morbi luctus ultrices sodales. Integer pulvinar ligula et erat ultrices, non placerat eros condimentum. Proin sagittis interdum justo, sit amet lacinia odio consequat sed. Aenean malesuada libero vitae efficitur tristique. Etiam dictum laoreet lorem, id faucibus felis bibendum id. Aenean tincidunt eros sem, nec vulputate eros porttitor fringilla. Phasellus justo mauris, porttitor in metus eget, hendrerit aliquam justo.
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut volutpat velit. Morbi luctus ultrices sodales. Integer pulvinar ligula et erat ultrices, non placerat eros condimentum. Proin sagittis interdum justo, sit amet lacinia odio consequat sed. Aenean malesuada libero vitae efficitur tristique. Etiam dictum laoreet lorem, id faucibus felis bibendum id. Aenean tincidunt eros sem, nec vulputate eros porttitor fringilla. Phasellus justo mauris, porttitor in metus eget, hendrerit aliquam justo."""
    },

    {
        "slug": "nature-is-the-best",
        "image": "mountains.jpg",
        "author": "Zaryab Ahmed",
        "date": date(2021, 7, 21),
        "title": "Nature At Its Best",
        "excerpt": "There's nothin like the views you get when hiking in the mountains! And I was't even prepared for what happened whilst I was enjoying the view!",
        "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut volutpat velit. Morbi luctus ultrices sodales. Integer pulvinar ligula et erat ultrices, non placerat eros condimentum. Proin sagittis interdum justo, sit amet lacinia odio consequat sed. Aenean malesuada libero vitae efficitur tristique. Etiam dictum laoreet lorem, id faucibus felis bibendum id. Aenean tincidunt eros sem, nec vulputate eros porttitor fringilla. Phasellus justo mauris, porttitor in metus eget, hendrerit aliquam justo.

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut volutpat velit. Morbi luctus ultrices sodales. Integer pulvinar ligula et erat ultrices, non placerat eros condimentum. Proin sagittis interdum justo, sit amet lacinia odio consequat sed. Aenean malesuada libero vitae efficitur tristique. Etiam dictum laoreet lorem, id faucibus felis bibendum id. Aenean tincidunt eros sem, nec vulputate eros porttitor fringilla. Phasellus justo mauris, porttitor in metus eget, hendrerit aliquam justo.
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut volutpat velit. Morbi luctus ultrices sodales. Integer pulvinar ligula et erat ultrices, non placerat eros condimentum. Proin sagittis interdum justo, sit amet lacinia odio consequat sed. Aenean malesuada libero vitae efficitur tristique. Etiam dictum laoreet lorem, id faucibus felis bibendum id. Aenean tincidunt eros sem, nec vulputate eros porttitor fringilla. Phasellus justo mauris, porttitor in metus eget, hendrerit aliquam justo."""
    }
]

# Helper function


def get_date(post):
    return post["date"]

# Create your views here.


def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html")


def post(request, slug):
    return render(request, "blog/post-detail.html")
