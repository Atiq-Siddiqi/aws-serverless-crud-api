---

## ⚡ Performance Optimization & Load Testing (Optional Module)

This module focuses on the **Performance Efficiency** and **Cost Optimization** pillars of the AWS Well-Architected Framework by profiling resource thresholds.

### 1. AWS Lambda Power Tuning
We utilize the `aws-lambda-power-tuning` Serverless Application Repository execution state machine to benchmark cost vs. performance over variable resource profiles ($128\text{ MB}$ to $1024\text{ MB}$).

To replicate this optimization test:
1. Deploy the power tuning application via AWS SAM / CloudFormation.
2. Execute the state machine using the input format structured in `test-payloads/lambda-power-tuning-input.json`.
3. Analyze the output visualization payload to assess the execution cost curve.

### 2. Postman Benchmarking & Load Results
A baseline load test was performed using Postman collections targeting the deployed API Gateway endpoint. 

| Metric Configuration | Baseline Setup | Optimized Setup |
| :--- | :--- | :--- |
| **Allocated Compute Memory** | 128 MB | 1024 MB |
| **Configured Timeout** | Default | 5.0 Seconds |
| **Performance Delta** | Higher Latency | Significantly Faster Response Time |

**Conclusion:** Because AWS scales available vCPU linearly alongside memory allocations, increasing compute boundaries to $1024\text{ MB}$ relieves payload serialization bottlenecks, drastically reducing transaction processing windows.
