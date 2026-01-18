import base64
import re

# Maximum allowed resume size (in megabytes)
MAX_SIZE_MB = 2


def validate_application(data: dict) -> tuple[bool, str]:
    """
    Validates required application fields and email format.

    Args:
        data: Dictionary containing application fields.

    Returns:
        (True, "") if valid, otherwise (False, error_message).
    """
    required_fields = ["name", "email", "position"]

    for field in required_fields:
        if not data.get(field):
            return False, f"{field} is required"

    # Basic email format validation
    if not re.match(r"[^@]+@[^@]+\.[^@]+", data["email"]):
        return False, "Invalid email format"

    return True, ""


def validate_resume(resume_base64: str) -> tuple[bool, str]:
    """
    Validates a base64-encoded PDF resume.

    Ensures the resume:
    - Is valid base64
    - Does not exceed the maximum size
    - Is a PDF file

    Args:
        resume_base64: Base64-encoded resume string.

    Returns:
        (True, "") if valid, otherwise (False, error_message).
    """
    try:
        # Strip data URL prefix if present
        if "," in resume_base64:
            resume_base64 = resume_base64.split(",", 1)[1]

        file_data = base64.b64decode(resume_base64)

        size_mb = len(file_data) / (1024 * 1024)
        if size_mb > MAX_SIZE_MB:
            return False, f"Resume exceeds {MAX_SIZE_MB}MB limit"

        # PDF files start with the "%PDF" signature
        if not file_data.startswith(b"%PDF"):
            return False, "Resume must be a PDF"

    except Exception:
        return False, "Invalid base64 resume"

    return True, ""
