from django.shortcuts import render, redirect
from .models import Article

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate

from .forms import ArticleForm

# Create your views here.
def home(request):
    articles = Article.objects.all().order_by("-created_at")
    q = request.GET.get("q")
    if request.GET.get("q") is not None:

        articles = Article.objects.filter(
            Q(user__first_name__icontains=q)
            | Q(title__icontains=q)
            | Q(category__title__icontains=q)
        ).order_by("-created_at")

    else:
        q = ""

    context = {"articles": articles}
    return render(request, "home.html", context)


def article(request, slug):
    article = Article.objects.get(slug=slug)
    context = {"article": article}
    return render(request, "article.html", context)


@login_required(login_url="login")
def create(request):

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            if form.is_valid():
                # form.save() returns a model instance, not another form
                article = form.save(commit=False)
                article.user = request.user
                article.save()
                form.save_m2m()

            return redirect("home")

    form = ArticleForm()
    form.order_fields(field_order=["title", "body", "image", "category"])
    context = {"form": form}
    return render(request, "article_form.html", context)


@login_required(login_url="login")
def delete_article(request, slug):
    article = Article.objects.get(slug=slug)

    if request.method == "POST":
        article.delete()
        return redirect("home")

    context = {"obj": article}
    return render(request, "deletepage.html", context)


@login_required(login_url="login")
def update_article(request, slug):
    article = Article.objects.get(slug=slug)

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            form.save_m2m()
            return redirect("article", slug=article.slug)

    form = ArticleForm(instance=article)
    context = {"form": form}
    return render(request, "article_form.html", context)
