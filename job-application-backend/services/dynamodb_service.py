import os
from datetime import datetime

import boto3

# Configuration via environment variables for flexibility across environments
TABLE_NAME = os.environ.get("TABLE_NAME", "JobApplications-AfA")
REGION = os.environ.get("REGION", "us-east-2")

# Initialize DynamoDB table
dynamodb = boto3.resource("dynamodb", region_name=REGION)
table = dynamodb.Table(TABLE_NAME)


def save_application(
    application_id: str,
    name: str,
    email: str,
    position: str,
    resume_url: str,
    status: str = "submitted",
) -> None:
    """
    Saves a job application record to DynamoDB.

    Args:
        application_id: Unique identifier for the application.
        name: Applicant's full name.
        email: Applicant's email address.
        position: Job position applied for.
        resume_url: URL to the applicant's resume.
        status: Application status (default: "submitted").
    """
    table.put_item(
        Item={
            "application_id": application_id,   # Partition key
            "name": name,
            "email": email,
            "position": position,
            "resume_url": resume_url,
            "status": status,
            "created_at": datetime.utcnow().isoformat(),
        }
    )
