## Overview 

flask-mercadopago-notifications-receiver is a simple webhook receiver Flask API designed to receive notifications from MercadoPago and to send them to an Amazon SQS queue. This example project is a good starting point for developers who are new to MercadoPago and Amazon SQS.

## Usage

Before using this project, you need to create a `.env` file in the root folder and add your AWS credentials. You also have to set up a webhook endpoint in your MercadoPago account to point to the Flask API. Additionally, you need to specify the queue where you want to receive your notifications.

You will also need to install the required dependencies with pip:

```sh
pip3 install -r requirements.txt
```

Once you have configured your `.env` file and installed the required dependencies, you can start the API by running:

```sh
python3 app.py
```

## Configuration

In the `.env` file, you need to set the following variables:

- `AWS_ACCESS_KEY_ID`: the Access Key ID for your AWS account.
- `AWS_SECRET_ACCESS_KEY`: the Secret Access Key for your AWS account.
- `AWS_DEFAULT_REGION`: the region where your Amazon SQS queue is located.
- `AWS_SQS_QUEUE_URL`: the URL of the Amazon SQS queue where you want to receive notifications.

## Contributing

If you find any issues or want to contribute to this project, feel free to create a pull request or open an issue in the repository. We welcome any contributions that can help improve this project.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.