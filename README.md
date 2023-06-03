## Overview
This repository contains an example Flask API that can receive notifications from MercadoPago and send them to an Amazon SQS queue. The purpose of this project is to provide developers with a starting point for building their own notification receivers.

## Setup
Before running this project, you will need to create a `.env` file in the root folder and add your Amazon Web Services and MercadoPago credentials. The required variables are:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- AWS_SQS_QUEUE_URL
- MP_ACCESS_TOKEN
- MP_PUBLIC_KEY
- MP_WEBHOOK_SECRET

Once you have added your credentials, you can install the required dependencies by running:

```
pip install -r requirements.txt
```

## Usage
To run the Flask app, use the following command:

```
flask run
```

This will start the app and make it accessible at http://localhost:5000 by default. The app has two endpoints:

- `/mercadopago/notifications`: This endpoint is where MercadoPago will send notifications. When a notification is received, it will be added to the specified SQS queue.
- `/test`: This endpoint can be used to test that the app is working correctly. It will send a test message to the specified SQS queue.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.