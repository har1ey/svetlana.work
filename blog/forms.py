
from django import forms
from blog.models import Article, Order
from ckeditor.widgets import CKEditorWidget
from nocaptcha_recaptcha.fields import NoReCaptchaField
from nocaptcha_recaptcha.widgets import InvisibleReCaptchaWidget

class ArticleForm(forms.ModelForm):

    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ['article_text', ]


class OrderForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Article.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = Order
        fields = ['product', 'name', 'phone']
