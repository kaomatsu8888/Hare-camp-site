from http.client import HTTPResponse
from django.shortcuts import render, redirect

from blog.forms import CommentForm
from .models import Post

def frontpage(request): #requestはユーザーからのリクエスト
    posts = Post.objects.all() #Postモデルのオブジェクトを全て取得
    return render(request, "blog/frontpage.html" , {"posts": posts}) #render関数は第一引数にrequest、第二引数にテンプレート名、第三引数にテンプレートに渡すデータを辞書型で指定する

def post_detail(request, slug): #slugはURLの一部として使われる.slugはpost-1が入る。下のpostに入る。同じだったらpost_detail.htmlをリターンで返す
    post = Post.objects.get(slug=slug) #Postモデルのオブジェクトを取得.getは一つのオブジェクトを取得するメソッド

    if request.method == "POST": #POSTメソッドでリクエストが送られてきたらformを作成する
        form = CommentForm(request.POST) #formという変数を用意して、importしたCommentFormを代入しrequest.POSTを引数に渡す

        if form.is_valid(): #フォームが有効かどうか、is_valid()関数を使って確認する
            comment = form.save(commit=False) #commit=Falseはデータベースに保存しないという意味。
            comment.post = post #comment.postにpostを代入する。postは上のpost = Post.objects.get(slug=slug)で取得したオブジェクト
            comment.save() #commentを保存する

            return redirect("post_detail", slug=post.slug) #コメントを飛ばしたときにredirecはどこに飛ばすかを指定。現在のページの詳細ページに飛ばす
        
    else: #POSTメソッドでリクエストが送られてきていない場合はformを作成する
        form = CommentForm() #formという変数を用意して、importしたCommentFormを代入する
        
    return render(request, "blog/post_detail.html", {"post": post, "form": form})  #render関数は第一引数にrequest、第二引数にテンプレート名、第三引数にテンプレートに渡すデータを辞書型で指定する
