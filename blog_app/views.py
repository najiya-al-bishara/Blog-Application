from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog_app.forms import UserAddForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from.models import Bloglist,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.shortcuts import get_object_or_404



# Create your views here.
def first(request):
    # return HttpResponse('hello world')
    return render (request,'home.html')


def view_blog(request):
    blogs=Bloglist.objects.all().order_by("-Publish_date")
    p=Paginator(blogs,5)
    page_number=request.GET.get("page")
    try:
        page_obj=p.get_page(page_number)
    except PageNotAnInteger:
        page_obj=p.page(1)    
    except EmptyPage:
        page_obj=p.page(p.num_pages)
            
    
    return render(request,"viewblogs.html",{"page_obj":page_obj})

CATEGORY_CHOICES=(
    
    ('Fashion','Fashion&styles'),
    ('Business','Business'),
    ('Social','Social'),
    ('Travel','Travel'),
    ('Food','Food'),
    ('Culture','Culture'),
    ('Nature','Nature'),
)

def add_blog(request):
     if request.method=='POST':
        blog=Bloglist(Publish_date=request.POST["Publish_date"],Author_name=request.POST["Author_name"],Blog_title=request.POST["Blog_title"],Blog_caption=request.POST["Blog_caption"])
        blog.Blog_image=request.FILES.get("Blog_image")
        blog.Blog_category=request.POST.get("Blog_category")
        blog.save()
        messages.info(request,"successfully added")
        return redirect("view_blog")
     return render(request,"add-blog.html",{'category_choices':CATEGORY_CHOICES})

CATEGORY_CHOICES=(
   
    ('Fashion','Fashion&styles'),
    ('Business','Business'),
    ('Social','Social'),
    ('Travel','Travel'),
    ('Food','Food'),
    ('Culture','Culture'),
    ('Nature','Nature'),
)


def category_view(request,cate_code):
    category_blogs=[]
    for code,name in CATEGORY_CHOICES:
        if code==cate_code:
            blogs=Bloglist.objects.filter(Blog_category=code)
            category_blogs.append({'category_name':name,'blogs':blogs})
            break
        context={'category_blogs':category_blogs,}
    return render(request,'category.html', context)


    



# delete blog
def deleteblog(request,pk):
    edit=Bloglist.objects.get(Blog_id=pk)
    edit.delete()
    messages.info(request,"deleated")
    return redirect("view_blog")

def contact(request):
    return render(request,'contact.html')

def my_page(request):
    myblog=Bloglist.objects.filter(Author_name=request.user.username)
    print(myblog)

    return render(request,'viewmy_blog.html',{'myblog':myblog})

#about
def about(request):
    return render(request,'about.html')


#like
def like(request,Blog_id):
    blog=get_object_or_404(Bloglist,Blog_id=Blog_id)
    if request.method=="POST":
        if request.user in blog.likes.all():
            blog.likes.remove(request.user)
        else:
            blog.likes.add(request.user)
    return redirect("view_blog")
#edit
def edit(request,vid):
    single_blog=Bloglist.objects.get(Blog_id=vid)
    if request.method == "POST":
        single_blog.Blog_title=request.POST["Blog_title"]
        single_blog.Blog_caption=request.POST["Blog_caption"]
        single_blog.Blog_category=request.POST["Blog_category"]
        if "Blog_image" in request.FILES:
            single_blog.Blog_image=request.FILES["Blog_image"]
        single_blog.save()
        return redirect("view_blog")
    return render(request,"edit.html",{"single_blog":single_blog}) 

#comment section
def blog_comment(request,blog_id):
    blog=get_object_or_404(Bloglist,Blog_id=blog_id)
    comments=Comment.objects.filter(blog=blog).order_by('-timestamp')[:2]
    remaining_comments=Comment.objects.filter(blog=blog).order_by('-timestamp')[2:]
    if request.method == "POST":
        authorname=blog.Author_name
        content=request.POST.get('content')
        comment=Comment(blog=blog, authorname=authorname,content=content)
        comment.save()
        return redirect('blog_comment',blog_id=blog_id)
    return render(request,'viewmy_blog.html',{'blog':blog,'comments':comments,'remaining_comments':remaining_comments})

        



    











