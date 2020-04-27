from django.urls import path,include
from django.contrib.auth import views as auth_views
from accounts import views
from .views import(
    # restricted,
    # table_post,
    table_get,
    # ChangePasswordView,
    ReadFile,
)

urlpatterns =[
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('table/', table_get.as_view(),name='list'),
    # path('passwordchange/', ChangePasswordView.as_view(),name='update'),
    path('readfile/', ReadFile.as_view()),
    path('',include('django.contrib.auth.urls')),
    #ChangePasswordView
    # path('restricted/',views.restricted),
    # path('tablelist/',table_post.as_view(),name='create'),
    # path('tabledata/',views.table_post),
    # url(r'^company/', views.companyApi),
    
    
]