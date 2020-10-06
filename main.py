#!/usr/bin/env python
import os

from cdktf import App, TerraformStack
from constructs import Construct

from imports.archive import DataArchiveFile
from imports.aws import AwsProvider, IamRole, LambdaFunction


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AwsProvider(self, "aws-provider", region="us-west-2")

        role = IamRole(
            self,
            "cdktf-iam-role",
            assume_role_policy="""{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
""",
        )

        archive = DataArchiveFile(
            self,
            "cdktf-data-file",
            output_path=f"{os.path.dirname(os.path.abspath(__file__))}index.zip",
            type="zip",
            source_content_filename="index.py",
            source_content="""
def handler(event, context):
    print("Hi data archive")
""",
        )

        LambdaFunction(
            self,
            "cdktf-lambda-function",
            function_name="cdktf-lambda-function",
            handler="index.handler",
            role=role.arn,
            runtime="python3.8",
            filename=archive.output_path,
            timeout=20,
            memory_size=256,
        )


app = App()
MyStack(app, "cdktf-investigation")

app.synth()
