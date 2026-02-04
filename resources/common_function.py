from rest_framework.response import Response

def generate_response(
    status_code,
    message,
    data=None,
    error_message=None
):
    response = {
        "status": status_code,
        "message": message,
        "data": data,
        "error": error_message
    }
    return Response(response, status=status_code)
