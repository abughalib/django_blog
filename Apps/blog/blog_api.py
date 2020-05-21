from Apps.blog.models import Post
import os
from django_project import settings


def blog_api_generate():
    posts = Post.objects.all()
    BlogJson = os.path.join(settings.BASE_DIR, 'templates')
    BLOGJSON = os.path.join(BlogJson, 'blog')
    fileLocation = os.path.join(BLOGJSON, 'api.json')
    myjson = open(fileLocation, mode='w', encoding='UTF-8')
    myjson.write("[")

    for post in posts:
        myjson.write('{')
        myjson.write(f'"id":{post.pk}, "title":{post.title}, "content":{post.content}, "author":{post.author}')
        myjson.write('},')
    myjson.write("]")
