from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import APIService

# Initialize the API service with a  third-party auth service URL
auth_service_url = "http://127.0.0.1:8000"
api_service = APIService(auth_service_url)

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = api_service.authenticate_user(user_id)
            return Response({"token": token}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
