## Introduction
This repository contains an example Flask API application that receives notifications from MercadoPago, a payment gateway service, and sends them to an Amazon Simple Queue Service (SQS) queue. This application can be used as a starting point to integrate MercadoPago with AWS services.

## Prerequisites
Before using this application, you need to have the following:
- An AWS account with access to SQS
- A MercadoPago account with a WebHook configured to send notifications to your API endpoint
- Python 3.6 or later on your development environment

## Installation
1. Clone the repository to your local machine
2. Install the required packages using `pip install -r requirements.txt`
3. Create a `.env` file in the root folder, and add the following environment variables:
    1. `AWS_ACCESS_KEY_ID`: The access key ID for your AWS account
    2. `AWS_SECRET_ACCESS_KEY`: The secret access key for your AWS account
    3. `AWS_DEFAULT_REGION`: The AWS region for your SQS queue
    4. `AWS_SQS_QUEUE_URL`: The URL of your SQS queue
4. Run the application using `python app.py`

## Usage
The Flask application runs on port `5000` by default. To test the application, you can send a POST request to the `/notifications` endpoint with a JSON payload containing the MercadoPago notification.

When the request is received by the application, it will send the notification to the SQS queue specified in the `.env` file.

## Contributing
Contributions are welcome! If you find any issues or have a suggestion for improvement, please create an issue or submit a pull request.

## License
This application is licensed under the MIT License. See the LICENSE file for more details.