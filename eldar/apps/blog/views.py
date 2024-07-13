from django.shortcuts import render, redirect
from  .models import News, Languages, Topic, Comments

def home(request):
   lang = Languages.objects.all()
   return render(request, 'blog/index.html', {'lang': lang})


def news(request, title_id):
   news = Topic.objects.get(id=title_id)
   title = News.objects.get(title=news)


   if request.method == 'POST':
      name = request.POST['fname']
      comment_ = request.POST['message']
      Comments.objects.create(name=name, message=comment_, news=title)

      return redirect('blog:news', title_id)

   comment = Comments.objects.filter(news=title)
   #print(comment)


   return render(request, 'blog/news.html', {'news': news, 'title': title, 'comment':comment})
