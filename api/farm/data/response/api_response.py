from rest_framework.response import Response

class ApiResponse(Response):
    def __init__(self, body=None, status_code=200, narration="Success", successful=True):
        response_data = {
            "successful": successful,
            "narration": narration,
            "status": status_code,
            "body": body
        }
        super().__init__(data=response_data, status=status_code)
