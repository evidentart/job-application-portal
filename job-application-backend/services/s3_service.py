import base64
import os

import boto3

# Configuration via environment variables
BUCKET_NAME = os.environ.get("BUCKET_NAME", "jobapplications-afa")
REGION = os.environ.get("REGION", "us-east-2")

# Initialize S3 client
s3 = boto3.client("s3", region_name=REGION)


def upload_resume(resume_base64: str, application_id: str) -> str:
    """
    Uploads a base64-encoded PDF resume to S3 and returns a presigned URL.

    Args:
        resume_base64: Base64-encoded PDF resume (with or without data URL prefix).
        application_id: Unique identifier used as the S3 object key.

    Returns:
        A presigned URL valid for 24 hours that allows temporary access to the resume.
    """
    # Strip data URL prefix if present (e.g. "data:application/pdf;base64,")
    if "," in resume_base64:
        resume_base64 = resume_base64.split(",", 1)[1]

    # Decode base64 string into binary PDF data
    pdf_data = base64.b64decode(resume_base64)

    # Store the resume using the application ID as the filename
    key = f"{application_id}.pdf"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=pdf_data,
        ContentType="application/pdf",
    )

    return s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": BUCKET_NAME, "Key": key},
        ExpiresIn=86400,  # 24 hours
    )
