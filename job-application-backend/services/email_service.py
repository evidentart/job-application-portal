import os

import boto3

# Configuration via environment variables
ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL", "hr@example.com")
REGION = os.environ.get("REGION", "us-east-2")

# Initialize the SES client for sending emails
ses = boto3.client("ses", region_name=REGION)


def send_notification(
    name: str,
    email: str,
    position: str,
    resume_url: str,
) -> None:
    """
    Sends a notification email to HR/admin when a new application is submitted.

    Args:
        name: Applicant's full name.
        email: Applicant's email address.
        position: Job position applied for.
        resume_url: URL to the applicant's resume.
    """
    html_body = f"""
    <h2>New Job Application</h2>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Position:</strong> {position}</p>
    <p><a href="{resume_url}">View Resume</a></p>
    """

    ses.send_email(
        Source=ADMIN_EMAIL,
        Destination={"ToAddresses": [ADMIN_EMAIL]},
        Message={
            "Subject": {"Data": "New Job Application"},
            "Body": {"Html": {"Data": html_body}},
        },
    )


def send_confirmation(
    to_email: str,
    name: str,
    position: str,
) -> None:
    """
    Sends an application confirmation email to the applicant.

    Args:
        to_email: Applicant's email address.
        name: Applicant's full name.
        position: Job position applied for.
    """
    html_body = f"""
    <h2>Application Received</h2>
    <p>Hello {name},</p>
    <p>Thank you for applying for the <strong>{position}</strong> role.</p>
    <p>We’ll be in touch if you’re shortlisted.</p>
    """

    ses.send_email(
        Source=ADMIN_EMAIL,
        Destination={"ToAddresses": [to_email]},
        Message={
            "Subject": {"Data": "Your Application Was Received"},
            "Body": {"Html": {"Data": html_body}},
        },
    )
