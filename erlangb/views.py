from .models import Erlangb
from .serializers import ErlangBSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
@api_view(['POST'])
def holdingTime(request):
    data ={}
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        offerLoad = float(data.get("offerLoad"))
        arrivalRate = float(data.get("arrivalRate"))
        
        answer = (offerLoad / arrivalRate) * 3600
        
        print(answer)
        data.update({"holdTime": offerLoad})
        data.update({"arrivalRate": arrivalRate})
        data.update({"answer": answer})
        serializer = ErlangBSerializer(data=data)
        if serializer.is_valid():
            print(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def offeredLoad(request):
    data ={}
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        holdTime = float(data.get("holdTime"))
        arrivalRate = float(data.get("arrivalRate"))
        
        answer = (holdTime * arrivalRate) / 3600

        print(answer)
        data.update({"holdTime": holdTime})
        data.update({"arrivalRate": arrivalRate})
        data.update({"answer": answer})
        serializer = ErlangBSerializer(data=data)
        if serializer.is_valid():
            print(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def arrivalRate(request):
    data ={}
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        offerLoad = float(data.get("offerLoad"))
        holdTime = float(data.get("holdTime"))
        
        answer = (offerLoad / holdTime) * 3600

        print(answer)
        data.update({"holdTime": offerLoad})
        data.update({"holdTime": holdTime})
        data.update({"answer": answer})
        serializer = ErlangBSerializer(data=data)
        if serializer.is_valid():
            print(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name="dispatch")
class BlockingProbability(APIView):
    def factorial(self,n):
        if n == 1:
            return n
        elif n == 0:
            return 1
        elif n < 1:
            return ("NA")
        else:
            return n * self.factorial(n-1)
    
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        offerLoad = float(data.get("offerLoad"))
        channelNum = int(data.get("channelNum"))

        fact = self.factorial(channelNum)

        print(fact)

        top = (offerLoad ** channelNum) / fact

        sum = 0
        data = {}
        for i in range(channelNum + 1):
            factor = self.factorial(int(i))
            sum = sum + ((offerLoad ** int(i))/ factor)
        
        answer = top/sum

        data.update({"answer": answer})
        serializer = ErlangBSerializer(data=data)

        if serializer.is_valid():
            print(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class NumChannel(APIView):
    def computeRecursive (self, n,load, pn_1):
        return (load * pn_1) / (n + load * pn_1)

    def findMinServers(self,load, blockingProb):
        if (blockingProb == 1.0) or (load == 0.0):
            return 0
        pn = 1.0
        n = 0
        while (pn > blockingProb):
            n = n + 1
            pn = self.computeRecursive(n, load, pn)
            print(pn)
        return n

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        prob = float(data.get("prob"))
        offerLoad = float(data.get("offerLoad"))

        print(offerLoad)

        answer  = self.findMinServers(offerLoad,prob)

        print(answer)
        data = {}

        data.update({"answer": answer})
        serializer = ErlangBSerializer(data=data)

        if serializer.is_valid():
            print(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)