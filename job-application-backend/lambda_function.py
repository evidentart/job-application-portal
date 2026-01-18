import json
import uuid
import logging

from services import s3_service, dynamodb_service, email_service
from utils import validation_util
from utils.response_util import create_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    AWS Lambda handler for submitting a job application.
    """
    # Handle CORS preflight requests
    if event.get("httpMethod") == "OPTIONS":
        return create_response(200, "CORS OK")

    try:
        if "body" not in event:
            return create_response(400, "Missing request body")

        data = json.loads(event["body"])

        # Validate required application fields
        valid, message = validation_util.validate_application(data)
        if not valid:
            return create_response(400, message)

        # Resume is mandatory
        resume_base64 = data.get("resume_base64")
        if not resume_base64:
            return create_response(400, "resume_base64 is required")

        valid, message = validation_util.validate_resume(resume_base64)
        if not valid:
            return create_response(400, message)

        name = data["name"]
        email = data["email"]
        position = data["position"]

        # Generate unique application ID
        application_id = str(uuid.uuid4())

        # Upload resume to S3
        resume_url = s3_service.upload_resume(
            resume_base64=resume_base64,
            application_id=application_id,
        )

        # Persist application data
        dynamodb_service.save_application(
            application_id=application_id,
            name=name,
            email=email,
            position=position,
            resume_url=resume_url,
        )
        logger.info("Application %s saved", application_id)

        # Notify HR/admin (non-blocking)
        try:
            email_service.send_notification(
                name=name,
                email=email,
                position=position,
                resume_url=resume_url,
            )
        except Exception as e:
            logger.warning("Failed to send HR notification: %s", e)

        # Send confirmation email to applicant (non-blocking)
        try:
            email_service.send_confirmation(
                to_email=email,
                name=name,
                position=position,
            )
        except Exception as e:
            logger.warning("Failed to send confirmation email: %s", e)

        return create_response(
            200,
            "Application submitted successfully",
            {"application_id": application_id},
        )

    except Exception:
        logger.exception("Unhandled error")
        return create_response(500, "Internal server error")
