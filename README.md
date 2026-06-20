# Serverless CRUD API & Performance Benchmarking Lab

A complete, production-ready guide to deploying and optimizing a decoupled serverless REST API on AWS. This project implements secure multi-action request routing using a single Python runtime handler and optimizes the deployment configurations using empirical load testing data.

## 🏗️ High-Level Architecture

The microservice leverages a completely serverless infrastructure pattern:

[Client App] --(HTTPS POST)--> [API Gateway] --> [AWS Lambda] --> [Amazon DynamoDB]
│
└──> [CloudWatch Logs]

1. **Amazon API Gateway:** Directs HTTP payload endpoints securely via a custom resource `/dynamodbmanager`.
2. **AWS Lambda Execution Engine:** Runs an optimized Python 3.13 handler processing multiple operations without monolith resource bloat.
3. **Amazon DynamoDB:** Stores non-relational table objects securely via partition key indexes.

---

## 🛠️ Step-by-Step Deployment Guide

### Step 1: Enforce Least-Privilege IAM Policies
To secure the backend, initialize a custom policy using the configurations in `iam-policy.json`. This scopes Lambda capabilities down exclusively to required DynamoDB table mechanics and CloudWatch logging permissions. Attach this policy to your Lambda service role (`lambda-apigateway-role`).

### Step 2: Implement the Lambda Router
Provision an AWS Lambda function from scratch (`LambdaFunctionOverHttps`) using **Python 3.13**. Swap out the boilerplate execution code with the routing block located in `lambda_function.py`. Ensure your custom IAM execution role is selected under the function settings.

### Step 3: Provision DynamoDB Table
Deploy an Amazon DynamoDB Table named exactly `lambda-apigateway`. Specify your Partition Key as `id` with a data type string.

### Step 4: Configure API Gateway
Create a **REST API** (`DynamoDBOperations`) inside the AWS API Gateway console. Build a resource pathway `/dynamodbmanager` and append a **POST** method pointing directly to your Lambda function backend. Deploy your configuration changes to a deployment stage called `Prod` and secure your functional **Invoke URL**.

---

## 📊 Phase 5: Optimization & Microservice Load Testing

This section addresses the **Performance Efficiency** and **Cost Optimization** pillars of the AWS Well-Architected Framework.

### 1. AWS Lambda Power Tuning Configuration
Using the AWS Step Functions execution framework (`aws-lambda-power-tuning`), the system was systematically profiled using 10 concurrent requests at variable resource boundaries: `128MB, 256MB, 512MB, and 1024MB`. 

Input benchmarks can be reproduced utilizing the template provided inside `/test-payloads/lambda-power-tuning-input.json`.

### 2. Postman Load Testing Validation
Real-world performance testing was captured over two primary deployment profiles to benchmark the vCPU resource scaling attributes of AWS Lambda:

| Configuration Metric | Baseline Specification | Optimized Specification |
| :--- | :--- | :--- |
| **Allocated Function Memory** | 128 MB | 1024 MB |
| **Execution Timeout Limit** | 3.0 Seconds (Default) | 5.0 Seconds |
| **Performance Experience** | Resource Constrained Latency | Accelerated Turnaround Time |

**Core Optimization Logic:** Because AWS allocates CPU runtime shares linearly corresponding to your selected memory footprint size, scaling configurations to **1024MB** gives the application runtime engine access to significantly faster vCPU execution pipelines, shortening overall user response windows.
