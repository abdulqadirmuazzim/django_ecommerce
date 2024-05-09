from django.contrib import admin
from .models import Comment, Subscription, product


# Register your models here.
class CommentModel(admin.ModelAdmin):
    list_display = ["name", "email", "message"]


class productModel(admin.ModelAdmin):
    list_display = ["Pname", "image", "price"]


admin.site.register(Comment, CommentModel)
admin.site.register(Subscription)
admin.site.register(product, productModel)
