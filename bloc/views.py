from django.shortcuts import render
from .models import Post


def post_view(request):
    # Retrieve all Post objects
    post_values = Post.objects.all()

    # Pass the queryset to the template
    return render(request, "post.html", {"post_key": post_values})

