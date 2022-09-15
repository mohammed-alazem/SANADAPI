from rest_framework.decorators import api_view

from .serializers import TeamNameSerializer, JudgeMarkSerializer
from arbitration.models import AudienceAward, Teams, JudgingMarks
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django.http import FileResponse


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def vote_excel(request):
    data = []
    for i in range(9):
        data.append((i + 1, AudienceAward.objects.filter(TeamNumber=i + 1).count()))

    data.sort(key=sort_key, reverse=True)

    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = []
    list3 = []
    for i in range(9):
        list2.append(TeamNameSerializer(Teams.objects.get(id=data[i][0])).data['Name'])
    print(list2)

    for i in range(9):
        list3.append(data[i][1])

    print(list3)

    col1 = "Rank"
    col2 = "TeamName"
    col3 = "Votes"
    data = pd.DataFrame({col1: list1, col2: list2, col3: list3})
    data.to_excel('votes.xlsx', sheet_name='sheet1', index=False)
    return FileResponse(open('votes.xlsx', 'rb'), status=status.HTTP_200_OK)


def sort_key(e):
    return e[1]


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def judge_excel(request):
    col1 = "Rank"
    col2 = "TeamName"
    col3 = "Votes"

    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = []
    list3 = []
    list_temp = []

    for i in list1:
        list_temp.append(
            (i, marks_avrage(JudgeMarkSerializer(JudgingMarks.objects.filter(TeamNumber=i), many=True).data)))
    print(list_temp)

    list_temp.sort(key=sort_key, reverse=True)

    for i in list_temp:
        list2.append(TeamNameSerializer(Teams.objects.get(id=i[0])).data['Name'])

    for i in list_temp:
        list3.append(i[1])

    data = pd.DataFrame({col1: list1, col2: list2, col3: list3})
    data.to_excel('judge.xlsx', sheet_name='sheet1', index=False)
    return FileResponse(open('judge.xlsx', 'rb'), status=status.HTTP_200_OK)


def marks_avrage(data):
    sum = 0
    if len(data) >= 3:
        for i in data[0]['MarkAndQuestions'].values():
            sum = sum + i
        for i in data[1]['MarkAndQuestions'].values():
            sum = sum + i
        for i in data[2]['MarkAndQuestions'].values():
            sum = sum + i
    return sum / 3
