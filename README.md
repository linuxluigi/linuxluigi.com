# new Linuxluigi.com Website (not online)

AWS Tutorial
https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/

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
