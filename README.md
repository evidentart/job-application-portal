# Job Application Backend (AWS Serverless)

A simple serverless backend for submitting job applications, built with **Python**, **AWS Lambda**, **API Gateway**, **CloudFront**, **S3**, **DynamoDB**, and **SES**.

This project is designed as an **entry-level backend/cloud portfolio project**, focusing on clean code, validation, and real-world AWS patterns.

---

## ✨ Features

* Submit job applications via REST API
* Resume upload (PDF only) using Base64 encoding
* Secure resume storage in S3 with presigned URLs
* Application data stored in DynamoDB
* Email notifications to HR/admin
* Confirmation email sent to applicants
* Input validation and consistent API responses

---

## 🧱 Architecture Overview

* **CloudFront** – CDN and secure public entry point
* **API Gateway** – HTTP API routing
* **AWS Lambda** – Application logic
* **Amazon S3** – Resume storage
* **Amazon DynamoDB** – Application persistence
* **Amazon SES** – Email notifications

---

## 📥 API Request Example

**POST** `/apply`

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "position": "Backend Developer",
  "resume_base64": "data:application/pdf;base64,JVBERi0xLjQKJ..."
}
```

> ⚠️ Resume is **required** and must be a PDF under 2MB.

---

## 📤 API Response Example

```json
{
  "message": "Application submitted successfully",
  "application_id": "c1b4c5e1-9a3d-4e2f-b1e2-9d8f1e2a1234"
}
```

---

## ⚙️ Environment Variables

```env
REGION=us-east-2
BUCKET_NAME=jobapplications-afa
TABLE_NAME=JobApplications-AfA
ADMIN_EMAIL=hr@example.com
```

---

## 🧪 Validation Rules

* Required fields: `name`, `email`, `position`, `resume_base64`
* Email format validation
* Resume must be:

  * Base64 encoded
  * PDF format
  * ≤ 2MB

---

## 🛠️ Tech Stack

* **Language:** Python
* **Compute:** AWS Lambda
* **API:** Amazon API Gateway
* **CDN:** Amazon CloudFront
* **Storage:** Amazon S3
* **Database:** Amazon DynamoDB
* **Email:** Amazon SES

---

## 🎯 Project Goals

* Demonstrate backend fundamentals
* Show practical AWS serverless usage
* Practice clean code and validation
* Build a realistic, interview-ready project

---

## 🚀 Future Improvements

* Authentication (Cognito)
* Application status updates
* Admin dashboard
* Unit tests

---

## 👤 Author

Built by **Ali Akcin** as a learning and portfolio project.
