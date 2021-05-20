from django.contrib import admin
from .models import Article, Scope, ScopesInArticle


class ScopesInArticleInline(admin.TabularInline):
    # model = CarShop.car.through
    model = ScopesInArticle
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ScopesInArticleInline
    ]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [
        ScopesInArticleInline
    ]
