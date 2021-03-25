# Amazon Kendra Automatic Scaling

This project contains source code and supporting files for a serverless application that will allow you to scale up and down autmatically your Amazon Kendra Enterprise Edition query capacity units.

You can deploy with the SAM CLI. 

It includes the following files and folders:

* template.yaml - A template that defines the application's AWS resources.
* src/app.py - The source code for the Lambda function that will be deployed.

The application uses several AWS resources, including AWS Lambda functions and Amazon EventBridge.

# Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

SAM CLI - Install the [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)


```
sam deploy --guided
```


# Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```
aws cloudformation delete-stack --stack-name automatic_scaling
```

# Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.
