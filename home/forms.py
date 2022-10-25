from django.forms import ModelForm
from .models import Article, Comment
from django import forms


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        exclude = ("user", "slug")


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
        widgets = {
            "body": forms.TextInput(
                attrs={
                    "placeholder": "Enter your comment",
                    "class": "comment-form-text",
                }
            ),
        }
        labels = {
            "body": "",
        }
