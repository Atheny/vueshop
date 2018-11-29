"""OnlineShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.views.static import serve
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from OnlineShop.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls
from goods import views as gview
from users import views as uview
from user_operation import views as uoview
import xadmin

router = routers.DefaultRouter()
router.register(r'categorys', gview.CategoryViewSet, base_name="categorys")
router.register(r'goods', gview.GoodsListViewSet, base_name='goods')
router.register(r'code', uview.SmsCodeViewset, base_name='code')
router.register(r'users',uview.UserViewSet, base_name='users')
# 配置用户收藏的url
router.register(r'userfavs', uoview.UserFavViewset, base_name="userfavs")


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('docs/', include_docs_urls(title='二歪求知')),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('media/<path:path>', serve, {'document_root':MEDIA_ROOT}),
    # 为了和前端相同 改成login了
    path('login/', obtain_jwt_token),
    path('', include(router.urls)),
]
