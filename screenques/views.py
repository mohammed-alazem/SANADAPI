from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import InterActionQuestionSerializers, TempListSerializers
from .models import TempList, InterActionQuestion


@api_view(['GET','POST','PUT','DELETE'])
def inter_action_question(request):
    if request.method == 'GET':
        team = InterActionQuestion.objects.all()
        if not team:
            return Response({"state": "Empty !!"}, status=status.HTTP_204_NO_CONTENT)
        serializer = InterActionQuestionSerializers(team,many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND, )

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = TempListSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"state": "OK"}, status=status.HTTP_201_CREATED)
        else:
            data = {"state": str(serializer.errors)}

        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def inter_action_question_move(request):
    response = redirect('/admin/screenques/templist/')
    if request.method == 'POST':
        if TempList.objects.filter(id=request.GET.get("id")).exists():
            temp = TempList.objects.get(id=request.GET.get("id"))
        else:
            return response
        serializer_temp = TempListSerializers(temp)
        temp.delete()
        serializer_inter_action_question = InterActionQuestionSerializers(data=serializer_temp.data)

        if serializer_inter_action_question.is_valid():
            serializer_inter_action_question.save()

            return response
        else:
            data = {"state": str(serializer_inter_action_question.errors)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def inter_action_question_delete(request):
    response = redirect('/admin/screenques/templist/')
    if request.method == 'POST':
        if TempList.objects.filter(id=request.GET.get("id")).exists():
            temp = TempList.objects.get(id=request.GET.get("id"))
        else:
            return response
        temp.delete()
        return response
