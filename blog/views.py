from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html',{})

# def = 메서드
# request를 넘겨 받아, render 메서드 호출
# render은 request와 blog/post_list.html이라는 템플릿을 리턴받아
# 리턴 내용을 브라우저에 보여줌
