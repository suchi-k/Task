# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.decorators import action, api_view
# from .models import (Book,Author,Rental)
# from .serializers import(BookSerializer,AuthorSerializer,RentalSerializer)
# # Create your views here.
# @api_view(['GET','PUT'])#
# @api_view(["GET","PUT","DELETE",])
# def get_book_list(request, book_id):
#     try:
#         book_obj = Book.objects.get(id=book_id)

#         if request.method == "GET":
#             serializer = BookSerializer(book_obj)
#             return Response({"data":serializer.data}, status=status.HTTP_200_OK)
#         if request.method == "PUT":
#             serializer = BookSerializer(book_obj, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"message":"Song object updated successfully", "data":serializer.data}, 
#                                 status=status.HTTP_200_OK)
#             else:
#                 return Response({"message":"Something went wrong", 'errors':serializer.errors}, 
#                                 status=status.HTTP_400_BAD_REQUEST)
            
#             if request.method == "DELETE":
#             book_obj.delete()
#             return Response({"message":"Song object deleted successfully"}, status=status.HTTP_200_OK)
        
#     except Exception as e:
#         return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)   

        