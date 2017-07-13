# new Linuxluigi.com Website (not online)

Documentation: http://linuxluigicom.readthedocs.io/en/latest/

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

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/linuxluigi/linuxluigi.com)

Default Admin login when using the deployment button:

* User: ```admin```
* Password: ```demopass```
* email: ```admin@example.com```

# Todo

* Add a heroku Button
* add cloudflare
* Docs
* * add Roadmap
* * add URL Pattern // API - Admin - Wagtail
* * add Deployment // Heroku
* * pull git repo from heroku https://kb.heroku.com/why-do-i-see-a-message-you-appear-to-have-cloned-an-empty-repository-when-using-heroku-git-clonecd 
* * AWS Account settings