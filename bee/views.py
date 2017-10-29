from django.shortcuts import render, HttpResponse
from bee import models


# Create your views here.

def index(request):
    obj = models.Article.objects.all()  # 查询文章表
    return render(request, 'index.html', {'article': obj})
    # 返回数据到index.html
