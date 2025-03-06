from rest_framework.views import exception_handler
from rest_framework import status
from ..data.response.api_response import ApiResponse

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return ApiResponse(
            successful=False,
            narration="ERROR",
            status_code=response.status_code,
            body=response.data
        )
    return response
