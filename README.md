## Overview

This project provides an example Flask API that receives notifications from MercadoPago and forwards them to an Amazon SQS queue. This can be used as a starting point for building your own integrations with MercadoPago and Amazon SQS.

## Setup

To use this project, you will need to create a `.env` file in the root folder and add your AWS and MercadoPago credentials. The following variables are required:

- `AWS_ACCESS_KEY_ID`: Your AWS access key ID
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key
- `AWS_DEFAULT_REGION`: The AWS region where your SQS queue is located
- `AWS_SQS_QUEUE_URL`: The URL of your SQS queue
- `MERCADOPAGO_CLIENT_ID`: Your MercadoPago client ID
- `MERCADOPAGO_CLIENT_SECRET`: Your MercadoPago client secret

Once you have set up your credentials, you can run the Flask server with the following command:

```
python app.py
```

## Usage

To receive notifications from MercadoPago, you need to set up a webhook in the MercadoPago dashboard that points to your Flask server's URL. For example, if your Flask server is running on `localhost:5000`, you can set the webhook URL to `http://localhost:5000/notifications`.

When MercadoPago sends a notification to your webhook, this Flask server will receive it and forward it to your configured SQS queue.

## Contributing

Contributions are welcome! If you find a bug or want to add a feature, please open an issue or submit a pull request. 

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.