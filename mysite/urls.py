from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")), #トップページへのリクエストはblog.urlsにリダイレクト
]

# blog/urls.pyを作成
from django.urls import path
from . import views

urlpatterns = {
    path('', vuews.post_list, name='post_list'), # トップページにリクエストが来たらviews.post_listへ
}