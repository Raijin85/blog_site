from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView
# Create your views here.

# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 3) #display 3 posts
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)  # if page is not an integer display first Page
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request,'vlog/post/list.html', {'page':page,'posts':posts })
#
#     #before pagination
#     # posts = Post.published.all()
#     # return render(request,'vlog/post/list.html', {'posts':posts})



class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'vlog/post/list.html'

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,
                            publish__day=day)
    return render(request,'vlog/post/detail.html',{'post':post})
