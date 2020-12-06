from django.shortcuts import render
from django.views.generic import View
from .models import Post

class IndexView(View):
  def get(self, request, *args, **kwargs):
    # Postデータを呼び出して降順に並び替え
    post_deta = Post.objects.order_by("-id")
    return render(request, 'app/index.html',{
      'post_deta' : post_deta,
    })

