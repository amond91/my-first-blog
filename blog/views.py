from django.shortcuts import render, get_object_or_404
from .models import Post, BookStore, Coupon
from django.utils import timezone
from .forms import PostForm, CouponForm
from django.shortcuts import redirect


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(len(posts))
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form},)


def coupon_main(request, pk):
    coupon = get_object_or_404(Coupon, pk=pk)
    if request.method == 'POST':
        form = CouponForm(request.POST, instance=coupon)
        # if form.is_vaild():
        coupon = form.save(commit=False)
        coupon.use_date = timezone.now()
        coupon.used = True
        coupon.save()
        return render(request, 'blog/coupon_used.html', {'coupon':coupon})
    else:
        form = CouponForm()

    if coupon.used:
        return render(request, 'blog/coupon_used.html', {'coupon': coupon})
    else:
        return render(request, 'blog/coupon_not_used.html', {'coupon':coupon, 'form':form})