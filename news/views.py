from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import News
from .serializers import NewsSerializer


@api_view(['GET'])
def main_page(request):
    list_of_news = News.objects.all()
    serializer = NewsSerializer(list_of_news, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def news_detail_view(request, id):
    details = News.objects.get(id=id)
    serializer = NewsSerializer(details, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def news_add_view(request):
    serializer = NewsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"Added": "News object was added"})


@api_view(['POST'])
def news_update_view(request, id):
    news = News.objects.get(id=id)
    serializer = NewsSerializer(instance=news, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def news_delete_view(request, id):
    news = News.objects.get(id=id)
    news.delete()
    return Response({"Deleted": "News object was deleted"})