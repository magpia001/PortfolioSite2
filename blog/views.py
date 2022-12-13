from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostList(ListView):
    model = Post
    # template_name = 'blog/post_list.html'  
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post
    # blog/post_detail.html : 클래스이름_detail.html은 template_name 값 생략 가능
    # template_name = 'blog/post_detail.html'  
