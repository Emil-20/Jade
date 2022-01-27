from django.conf import settings
from django.urls import re_path
from django.contrib.staticfiles.urls import static
from django.conf import settings
from app import views
from . import views
urlpatterns = [
    re_path(r'^$',views.index, name='index'),
    re_path(r'^hello$',views.hello, name='hello'),
    re_path(r'^login$',views.login, name='login'),
    re_path(r'^register$',views.register, name='register'),
    re_path(r'^logout$',views.logout, name='logout'),
    re_path(r'^boys$',views.boys, name='boys'),
    re_path(r'^girls$',views.girls, name='girls'),
    re_path(r'^kids$',views.kids, name='kids'),
    re_path(r'^ahome$',views.ahome, name='ahome'),
    re_path(r'^categ$',views.categ, name='categ'),
    re_path(r'^cat2$',views.cat2, name='cat2'),
    re_path(r'^items$',views.items, name='items'),
    re_path(r'^vcat1$',views.vcat1, name='vcat1'),
    re_path(r'^vcat2$',views.vcat2, name='vcat2'),
    re_path(r'^vitem$',views.vitem, name='vitem'),
    re_path(r'^savecat1$',views.savecat1, name='savecat1'),
    re_path(r'^savecat2$',views.savecat2, name='savecat2'),
    re_path(r'^deletecat1/(?P<cat1_id>\d+)/$',views.deletecat1, name='deletecat1'),
    re_path(r'^editcat1/(?P<cat1_id>\d+)/$',views.editcat1, name='editcat1'),
    re_path(r'^updatecat1/(?P<cat1_id>\d+)/$',views.updatecat1, name='updatecat1'),
    re_path(r'^saveitem$',views.saveitem, name='saveitem'),
    re_path(r'^deleteitem/(?P<i_id>\d+)/$',views.deleteitem, name='deleteitem'),
    re_path(r'^edititem/(?P<i_id>\d+)/$',views.edititem, name='edititem'),
    re_path(r'^updateitem/(?P<i_id>\d+)/$',views.updateitem, name='updateitem'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    