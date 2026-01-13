# Job Application Portal 

A serverless system to submit job applications with optional resume upload, built using **AWS Lambda, DynamoDB, S3, and SES**. Applicants are notified via email, and HR/admin receives submissions automatically. This project is designed to demonstrate practical AWS usage in a simple, real-world scenario, showcasing key serverless concepts such as input validation, secure file storage, email automation, and CORS handling.

---

## Features

- Collect applicant **name, email, position**, and optional PDF resume.
- Store applications in **DynamoDB**.
- Upload resumes to **S3** with presigned URLs.
- Send notification to **HR/admin** and confirmation to applicants via **SES**.
- Input validation and CORS enabled.

---

## Architecture

- **Frontend:** HTML/JS form submits JSON to API.
- **API Gateway → Lambda:** Validates data, uploads resume, saves application, sends emails.
- **DynamoDB:** Stores application data.
- **S3:** Stores uploaded resumes.
- **SES:** Sends notification and confirmation emails.

---



## Setup & Deployment

### Backend Setup

1. **Create an S3 Bucket**
   - Used for resume uploads  
   - Ensure *all public access is blocked*

2. **Create DynamoDB Table**
   - Table name: `JobApplications-AfA`  
   - Partition key: `application_id` (String)

3. **Verify Admin Email in SES**
   - Region: `us-east-1`

4. **Deploy Lambda Function**
   - Handles submissions  
   - Uploads resume to S3  
   - Sends emails via SES  

5. **Configure API Gateway**
   - Create REST API  
   - Endpoint: `POST /submit`  
   - Lambda proxy integration  
   - Enable CORS (`POST, OPTIONS`)

---

## Frontend Setup

1. Open `frontend/index.html`  
2. Replace `API_URL` with your API Gateway endpoint  
3. Submit the form to test the workflow

---

## License

MIT License — free to use, modify, and distribute.
