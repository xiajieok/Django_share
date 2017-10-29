from django.contrib import admin
from bee import models
#从APP导入

admin.site.register(models.Article)
admin.site.register(models.UserProfile)
admin.site.register(models.Tag)
admin.site.register(models.Category)