from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_details.html', {'post': post})

# def post_new(request):
#     form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})