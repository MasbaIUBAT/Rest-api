from. models import Category, BlogPost
from.serializers import CategorySerializer

from rest_framework.views import APIView
from rest_framework.response import Response 

class CategoryView(APIView):
	def get(self, request):
		queryset = Category.objects.all()
		serializer_class = CategorySerializer(queryset,many=True)
		return Response(serializer_class.data)

# Create your views here.
