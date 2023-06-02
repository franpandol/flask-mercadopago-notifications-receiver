## Description
This is an example project for a Flask API which can receive notifications from MercadoPago and then send them to an Amazon SQS queue. The API can be used to streamline the process of handling MercadoPago notifications and make it easier to manage those notifications within the context of an Amazon SQS queue.

## Configuration
To configure this project, you'll need to create a `.env` file in the root directory of the project. The `.env` file should contain the following fields:

- `AWS_ACCESS_KEY_ID`: The Access Key for your AWS account.
- `AWS_SECRET_ACCESS_KEY`: The Secret Access Key for your AWS account.
- `AWS_DEFAULT_REGION`: The default region for your AWS account.
- `AWS_SQS_QUEUE_URL`: The URL for your Amazon SQS queue.

## Installation
1. Clone this repository.
2. Create a virtual environment for the project: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`

## Usage
To start the Flask server, execute the following command:
```bash
flask run
```
Once the server is running, MercadoPago notifications can be sent to the following URL: `http://localhost:5000/notifications`.
These notifications will then be added to the Amazon SQS queue. 

## Contributing
If you want to contribute to this project, please follow these steps:
1. Fork this repository.
2. Create a new branch for your changes: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -am 'Add some feature'`
4. Push your changes to your fork: `git push origin my-feature-branch`
5. Submit a pull request to this repository. 

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.