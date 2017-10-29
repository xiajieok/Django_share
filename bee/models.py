from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime


# 标签表
class Tag(models.Model):
    class Meta:
        app_label = 'bee'
        verbose_name = '标签'
        verbose_name_plural = '标签'

    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


# 版块
class Category(models.Model):
    class Meta:
        app_label = 'bee'
        verbose_name = '分类目录'
        verbose_name_plural = '分类目录'

    name = models.CharField(max_length=40, unique=True)
    # 版块名称，字符类型，唯一
    alias = models.CharField(max_length=40)

    # 别名，对应中英文
    def __str__(self):
        return self.name


# 文章表
class Article(models.Model):
    author = models.ForeignKey(User)  # 作者
    title = models.CharField(max_length=200, unique=True)  # 标题
    brief = models.CharField(null=True, blank=True, max_length=255)  # 简介
    content = models.TextField(u"文章内容")
    md = models.TextField(u"文章内容-MD格式", default='')  # markdown内容
    tags = models.ForeignKey(Tag)  # 标签
    # 分类目录
    category = models.ForeignKey(Category)
    created_date = models.DateTimeField(default=timezone.now)  # 创建日期
    published_date = models.DateTimeField(blank=True, null=True)  # 发布日期
    status_choices = (('draft', u"草稿"),
                      ('published', u"已发布"),
                      ('hidden', u"隐藏"),
                      )
    status = models.CharField(choices=status_choices, default='published', max_length=32)  # 文章状态
    reprinted = models.CharField(default='http://www.mknight.cn', max_length=64)  # 装载地址，爬虫使用
    views = models.IntegerField(default='0')  # 点击量

    def publish(self):
        self.published_date = datetime.now().strftime("%Y-%m-%d %H:%I:%S")
        self.save()

    def __str__(self):
        return self.title


# 扩展user表
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    signature = models.CharField(max_length=255, blank=True, null=True)
    head_img = models.ImageField(height_field=150, width_field=150, blank=True, null=True)

    def __str__(self):
        return self.name
