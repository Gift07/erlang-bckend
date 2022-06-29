from .serializers import ErlangCSerializer
from erlangb.models import Erlangb
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


@method_decorator(csrf_exempt, name="dispatch")
class WaitingProbability(APIView):
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

        print(data)
        if channelNum > offerLoad:
            fact = self.factorial(channelNum)

            left = (offerLoad ** channelNum) / fact

            right = channelNum / (channelNum - offerLoad)

            product = left * right

            sum = 0
            data = {}

            for i in range(channelNum):
                factor = self.factorial(int(i))
                sum = sum + ((offerLoad ** int(i)) / factor)

            topVar = sum + product

            answer = product / topVar

            data.update({"answer": answer})
            serializer = ErlangCSerializer(data=data)

            if serializer.is_valid():
                print(serializer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        else:
           return Response({"answer":"number of channels must be greater than offered Load"}, status=status.HTTP_200_OK) 


@method_decorator(csrf_exempt, name='dispatch')
class NumServer(APIView):
    def computeRecursive (self, n,load, pn_1):
        return (load * pn_1) / (n + load * pn_1)

    def findMinServersBlocking(self, waitProb, load):
        print("here")
        if (waitProb == 1.0) or (load == 0.0):
            return 0

        pn = 1.0  #blocking prob. Erlang C
        B = 1.0  #blocking prob. Erlang B
        n = 0

        print(waitProb)
        while (pn > waitProb):
            print("while")
            n = n + 1
            print(n)
            B = self.computeRecursive(n, load, B)
            print(B)
            pn = n * B / (n - load * (1 - B))
        return n

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        prob = float(data.get("prob"))
        offerLoad = float(data.get("offerLoad"))

        print(data)
        answer  = self.findMinServersBlocking(prob, offerLoad)

        data = {}

        data.update({"answer": answer})
        serializer = ErlangCSerializer(data=data)

        if serializer.is_valid():
            print(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
