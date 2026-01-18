import json


def create_response(
    status_code: int,
    message: str,
    extra: dict | None = None,
) -> dict:
    """
    Creates a standardized HTTP response for API Gateway/Lambda integrations.

    Args:
        status_code: HTTP status code (e.g., 200, 400, 500).
        message: Short, user-facing response message.
        extra: Optional additional data to include in the response body.

    Returns:
        A dictionary formatted for API Gateway responses.
    """
    body = {"message": message}

    if extra:
        body.update(extra)

    return {
        "statusCode": status_code,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "POST,OPTIONS",
        },
        "body": json.dumps(body),
    }
