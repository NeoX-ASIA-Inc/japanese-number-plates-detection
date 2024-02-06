# Japanese number plates detection

## Usage

### Prerequisites

In order to package your dependencies locally with `serverless-python-requirements`, you need to have `Python3.10` installed locally. You can create and activate a dedicated virtual environment with the following command:

```bash
python3.10 -m venv ./venv
source ./venv/bin/activate
```

Alternatively, you can also use `dockerizePip` configuration from `serverless-python-requirements`. For details on that, please refer to corresponding [GitHub repository](https://github.com/UnitedIncome/serverless-python-requirements).

### Deployment

This example is made to work with the Serverless Framework dashboard, which includes advanced features such as CI/CD, monitoring, metrics, etc.

In order to deploy with dashboard, you need to first login with:

```
serverless login
```

install dependencies with:

```
npm install
```

and

```
pip install -r requirements.txt
```

and then perform deployment with:

```
serverless deploy
```

After running deploy, you should see output similar to:

```bash
Deploying aws-python-flask-api-project to stage dev (ap-northeast-1)

✔ Service deployed to stack aws-python-flask-api-project-dev (182s)

endpoint: ANY - https://xxxxxxxx.execute-api.ap-northeast-1.amazonaws.com
functions:
  api: aws-python-flask-api-project-dev-api (1.5 MB)
```

_Note_: In current form, after deployment, your API is public and can be invoked by anyone. For production deployments, you might want to configure an authorizer. For details on how to do that, refer to [httpApi event docs](https://www.serverless.com/framework/docs/providers/aws/events/http-api/).

### Invocation

After successful deployment, you can call the created application via HTTP:

```bash
curl https://xxxxxxx.execute-api.ap-northeast-1.amazonaws.com/dev/
```

Which should result in the following response:

```
{"message":"Hello from root!"}
```

Calling the `/hello` path with:

```bash
curl https://xxxxxxx.execute-api.ap-northeast-1.amazonaws.com/dev/hello
```

Should result in the following response:

```bash
{"message":"Hello from path!"}
```

If you try to invoke a path or method that does not have a configured handler, e.g. with:

```bash
curl https://xxxxxxx.execute-api.ap-northeast-1.amazonaws.com/dev/nonexistent
```

You should receive the following response:

```bash
{"error":"Not Found!"}
```

### Local development

You can install all needed dependencies with the following commands:

```bash
pip install werkzeug
pip install -r requirements.txt
export FLASK_ENV=development
```

At this point, you can run your application locally with the following command:

```bash
flask run
```

## License
Japanese Number Plates Deteaction is distributed under the MIT License, copyright (c) 2023 NeoX Asia
