from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


def serializer_save_to_response(serializer: Serializer, ok_status: int) -> Response:
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=ok_status)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
