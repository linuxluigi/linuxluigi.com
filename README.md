# Template for Django Wagtail - Not production ready

AWS Tutorial
https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/

```bash
$ django-admin.py startproject --template=https://github.com/linuxluigi/template-django-wagtail/archive/master.zip --name=Procfile helloworld
```
change helloworld to your project name


# Local development

Setting up local venv for Python 2

```bash
virtualenv venv
```

And for Python 3

```bash
virtualenv -p python3 venv
```

Install requirements:
```bash
pip install -r requirements.txt 
```


# AWS Settings

## S3 - CORS

Example Cors

```xml
<CORSConfiguration>
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
```

# Deployment

## Heroku



todo: update settings for heroku
add heroku tool to upload env
https://github.com/heroku/heroku-django-template/blob/master/project_name/settings.py

### Using Python 2.7?

Just update `runtime.txt` to `python-2.7.13` (no trailing spaces or newlines!).

## Deployment to Heroku

```bash
git init
git add -A
git commit -m "Initial commit"

heroku create
git push heroku master

heroku run python manage.py migrate
```

## Zappa - AWS Lamda 

https://github.com/Miserlou/Zappa

1. Create a AWS User with a VPC -> http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_IAM.html
2. generate zappa json
3. deploy your application
4. upload your env to lambda -> http://docs.aws.amazon.com/lambda/latest/dg/env_variables.html
5. Update
6. Use a coustom Domain

# Other Django Project Templates

* https://github.com/jpadilla/django-project-template
* https://github.com/heroku/heroku-django-template/

# License

MIT License

Copyright (c) 2017 Steffen Exler

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.