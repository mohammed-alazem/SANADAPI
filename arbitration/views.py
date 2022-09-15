from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import JudgingMarksSerializers, TeamsSerializers, AudienceAwardSerializers
from .models import Teams, JudgingMarks, AudienceAward


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def add_marks(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        temp = {
            "1": data['MarkAndQuestions'][0],
            "2": data['MarkAndQuestions'][1],
            "3": data['MarkAndQuestions'][2],
            "4": data['MarkAndQuestions'][3],
            "5": data['MarkAndQuestions'][4],
            "6": data['MarkAndQuestions'][5],
            "7": data['MarkAndQuestions'][6],
            "8": data['MarkAndQuestions'][7],
            "9": data['MarkAndQuestions'][8],
            "10": data['MarkAndQuestions'][9]

        }
        data['MarkAndQuestions'] = temp
        if not JudgingMarks.objects.filter(TeamNumber=data["TeamNumber"], JudgType=data["JudgType"]).exists():
            serializer = JudgingMarksSerializers(data=data)

            if serializer.is_valid():
                serializer.save()

                return Response(status=status.HTTP_200_OK, data={"state": "ok"})
            else:

                data = {"state": str(serializer.errors)}
                print(data)
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"state": "repeated data !!"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def teams(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = TeamsSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data={"state": "ok"})
        else:
            data = {"state": str(serializer.errors)}

        return Response(status=status.HTTP_204_NO_CONTENT, data=data)

    elif request.method == 'GET':
        if Teams.objects.filter(TeamNumber=request.GET.get("num")).exists():

            team = Teams.objects.get(TeamNumber=request.GET.get("num"))

        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"state": "not found!!"})

        serializer = TeamsSerializers(team)
        return Response(status=status.HTTP_302_FOUND, data=serializer)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def audience_award(request):
    if request.method == 'POST':

        data = JSONParser().parse(request)
        if not AudienceAward.objects.filter(ID_Audience=data["ID_Audience"]).exists():

            serializer = AudienceAwardSerializers(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED, data={"state": "ok"})
            else:
                data = {"state": str(serializer.errors)}
        else:
            data = {"state": "cant vote more than one time !!"}
        return Response(status=status.HTTP_400_BAD_REQUEST, data=data)
