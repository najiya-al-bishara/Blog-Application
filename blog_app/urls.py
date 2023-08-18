from django.urls import path
from. import views  

urlpatterns =[
    path('',views.first,name='first'),
    path('add_blog',views.add_blog,name='add_blog'),
    path('category/<str:cate_code>/',views.category_view,name='category_view'),
    path('view_blog',views.view_blog,name='view_blog'),
    path('deleteblog/<int:pk>',views.deleteblog,name='deleteblog'),
    path('contact',views.contact,name='contact'),
    path('myblog',views.my_page,name='myblog'),
    path('about',views.about,name='about'),
    path('add_blog',views.add_blog,name='addblog'),
    path('like/<int:Blog_id>/like/',views.like,name='like'),
    path('edit/<int:vid>',views.edit,name='edit'),
    path('blog_comment/<int:blog_id>',views.blog_comment,name='comment')

    
    

    
]