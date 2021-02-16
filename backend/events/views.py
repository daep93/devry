from django.shortcuts import get_object_or_404
from mysite.utils import jwt_encode
from rest_auth.models import TokenModel
from rest_framework.authtoken.models import Token
from mysite.app_settings import TokenSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import EventSerializer, EventListSerializer, EventMainSerializer, EventdetailSerializer, bookmarkSerializer
from .models import Event
from rest_framework import viewsets
from profiles.models import Profile
import datetime
from accounts.models import User

class PostViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


@api_view(['GET'])
def event_main_list(request):
    """
    Event Main 목록 불러오기

    ---
    """
    now = datetime.datetime.now()
    now_day=now.strftime('%Y-%m-%d %H:%M:%S'+'+00:00')

    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user = user

    if request.method == 'GET':
        events = Event.objects.filter(start__lte=now_day, end__gt=now_day, king="True").order_by('start')
        serializer = EventMainSerializer(events, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def event_list(request):
    """
    Event 목록 보기
    user=글 쓴 유저의 정보
    host_name=호스트의 정보
    ---
    """
    now = datetime.datetime.now()
    now_day=now.strftime('%Y-%m-%d %H:%M:%S'+'+00:00')

    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user = user
        
    if request.method == 'GET':
        # events = Event.objects.all()
        events = Event.objects.filter(end__gt=now_day).order_by('start')
        for event in events:
            event.bookmark_num = event.bookmark_users.count() 
            if event.bookmark_users.filter(id=request.user.pk).exists():
                event.bookmarked = "True"      
            else:
                event.bookmarked = "False"

            if str(event.start) <= now_day:
                event.state =  "Start"
            
            elif str(event.start) > now_day:
                event.state =  "Ready" 
            event.save()
        events = Event.objects.filter(end__gt=now_day).order_by('start')
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def event_list_create(request):
    """
    Event 글 생성
    start_day = 년,월,일 을 입력받음
    start= 년,월,일,시간 모두 입력받음
    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user = user
        
    if request.method == 'GET':
        events = Event.objects.all() 
        for event in events:
            event.bookmark_num = event.bookmark_users.count() 
            if event.bookmark_users.filter(id=request.user.pk).exists():
                event.bookmarked = "True"      
            else:
                event.bookmarked = "False"
            event.save() 
        events = Event.objects.all()
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data)
        
    else:
        profiles = Profile.objects.all()
        if profiles.filter(user_id=request.user.id).exists():
            pro=profiles.get(user_id=request.user.id)
            request.data['host'] = pro.id

        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def event_detail_update_delete(request, event_pk):
    """
    Event 상세보기, 수정, 삭제
    
    ---
    """
    now = datetime.datetime.now()
    now_day=now.strftime('%Y-%m-%d %H:%M:%S'+'+00:00')
    
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user

    event = get_object_or_404(Event, pk=event_pk)
    event.bookmark_num = event.bookmark_users.count()  # bookmark_num check
    event.viewed_num = event.viewed_num + 1 # viewed_num++
    event.save()
    # bookmark_check
    if event.bookmark_users.filter(pk=request.user.pk).exists():
        event.bookmarked="True"
    else:
        event.bookmarked = "False"
   
    if request.method == 'GET':
        if str(event.start) <= now_day:
                event.state =  "Start" 
        elif str(event.start) > now_day:
                event.state = "Ready"
        
        if str(event.end) < now_day:
                event.state = "end"
        event.save()

        serializer = EventdetailSerializer(event)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
    else:
        event.delete()
        return Response({ 'id': event_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def bookmark(request, event_pk):
    """
    Event 북마크 기능

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user = user
        
    event = get_object_or_404(Event, pk=event_pk)
    if request.method == 'GET':
        if event.bookmark_users.filter(pk=request.user.pk).exists():
            event.bookmarked="True"
            serializer = bookmarkSerializer(event)
        else:
            event.bookmarked="False"
            serializer = bookmarkSerializer(event)
        return Response(serializer.data)

    # user가 event 북마크 누른 전체유저에 존재하는지.
    if request.method == 'POST':
        if event.bookmark_users.filter(pk=request.user.pk).exists():
            # bookmark cancled
            event.bookmark_users.remove(request.user)
            return Response("bookmark cancled")
        else:
            # bookmark
            event.bookmark_users.add(request.user)
            return Response("bookmark")


@api_view(['GET'])
def event_mybookmark(request):
    """
    my bookmark 목록 불러오기

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user = user

    if request.method == 'GET':
        mark=[]
        events = Event.objects.all()
        for event in events:
            if event.bookmark_users.filter(id=request.user.pk).exists():
                mark.append(event)
        
        serializer = EventListSerializer(mark, many=True)
        return Response(serializer.data)
