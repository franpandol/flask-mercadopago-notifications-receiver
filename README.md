## About the project
This repository contains an example project for creating a Flask API that is capable of receiving notifications from MercadoPago and forwarding them to an Amazon SQS queue. 

## How to use the project
To use this project, you need to create a `.env` file at the root of the project and add the following credentials:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`
- `AWS_SQS_QUEUE_URL`

These credentials are required to authenticate with the Amazon Simple Queue Service (SQS) that is responsible for forwarding the notifications received from MercadoPago.

## Deploying the project
To deploy the project, you will need to follow these steps:

1. Clone the repository.
2. Set up your credentials in the `.env` file.
3. Install the required dependencies.
4. Run the application.

Here are the specific commands you need to run:

```bash
$ git clone https://github.com/<your username>/flask-mercadopago-notifications-receiver.git
$ cd flask-mercadopago-notifications-receiver
$ echo "AWS_ACCESS_KEY_ID=<your_access_key_id>" >> .env
$ echo "AWS_SECRET_ACCESS_KEY=<your_secret_access_key>" >> .env
$ echo "AWS_DEFAULT_REGION=<region>" >> .env
$ echo "AWS_SQS_QUEUE_URL=<queue_url>" >> .env
$ pip install -r requirements.txt
$ flask run
```

Once the application is running, you can start receiving notifications from MercadoPago and they will be forwarded to the specified SQS queue. 

## Contributing
Contributions are always welcome! If you'd like to contribute to this project, please open an issue or a pull request. 

## License
This project is licensed under the MIT License.