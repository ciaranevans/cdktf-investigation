# cdktf-investigation
Looking into CDKTF and how it works/handles

Currently the app just spins up a Lambda function whose code is inlined in the CDKTF app

**This example uses local state, it is not a production-like example**

# Requirements

List stolen from [here](https://learn.hashicorp.com/tutorials/terraform/cdktf-build-python?in=terraform/cdktf)

* Terraform v0.12+
* cdktf
* Node.js v12.16+
* Python v3.7+ and pipenv
* an AWS account and AWS Access Credentials

# How to use this repo

1. Initialise Terraform providers

```bash
$ pipenv run init
```

2. Diff CDKTF against AWS

```bash
$ pipenv run diff
```

3. Deploy CDKTF app into AWS

```bash
$ pipenv run deploy
```

4. Destroy CDKTF app

```bash
$ pipenv run destroy
```
