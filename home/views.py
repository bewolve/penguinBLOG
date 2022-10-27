from django.shortcuts import render, redirect
from .models import Article

from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import ArticleForm, CommentForm

# Create your views here.
def home(request):
    articles = Article.objects.all().order_by("-created_at")
    q = request.GET.get("q")
    if request.GET.get("q") is not None:

        articles = Article.objects.filter(
            Q(user__first_name__icontains=q) | Q(category__title__icontains=q)
        ).order_by("-created_at")

    else:
        q = ""

    context = {"articles": articles}
    return render(request, "home.html", context)


def article(request, slug):
    article = Article.objects.get(slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
            return redirect("article", article.slug)

    form = CommentForm()
    context = {"article": article, "form": form}
    return render(request, "article.html", context)


@login_required(login_url="login")
def create(request):
    if request.user.is_superuser:

        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                if form.is_valid():
                    # when commit=false, form.save() returns a model instance, not another form
                    article = form.save(commit=False)
                    article.user = request.user
                    article.save()
                    form.save_m2m()

                return redirect("home")

    else:
        return redirect("home")

    form = ArticleForm()
    form.order_fields(field_order=["title", "body", "image", "category"])
    context = {"form": form}
    return render(request, "article_form.html", context)


@login_required(login_url="login")
def delete_article(request, slug):

    if request.user.is_superuser:
        article = Article.objects.get(slug=slug)

        if request.method == "POST":
            article.delete()
            return redirect("home")

        context = {"obj": article}
    else:
        return redirect("home")
    return render(request, "deletepage.html", context)


@login_required(login_url="login")
def update_article(request, slug):
    if request.user.is_superuser:
        article = Article.objects.get(slug=slug)

        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                article = form.save(commit=False)
                article.user = request.user
                article.save()
                form.save_m2m()
                return redirect("article", slug=article.slug)
    else:
        return redirect("home")
    form = ArticleForm(instance=article)
    context = {"form": form}
    return render(request, "article_form.html", context)
