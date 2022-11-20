# Brit-Demo

Welcome to my interpretation of the task set.

I've implemented th backed on AWS lambda using the FastAPI framework. The data is stored in a postgres DB hosted on AWS using the RDS service. Credentials are stored in an environment variable and should have been provided directly should you wish to view the structure. I have used CRUDRouter to make the implementation go a little faster as it's a good fit for this use case.

The build is currently manually completed by executing the following commands in order:

```bash
poetry build
pip install -t dist/lambda . --upgrade
cd dist/lambda
static folder is copied from brit_demo into newly created lambda folder.
zip -x '*.pyc' -r ../lambda.zip .
cd ../..
```

The resulting .zip file is uploaded to a lambda. Unfortunately, I did not have time to build a pipeline.

## Testing
You'll notice that there aren't any tests in the repo. I am using well used libraries for brevity and simplicity. Therefore, there is very little home grown logic to test. If I were to implement a repo pattern then that would be thoroughly tested against the DB and the service layer.

The demo server is live here:
https://wps536osra.execute-api.us-east-2.amazonaws.com/dev/

