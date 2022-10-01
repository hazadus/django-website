# django-website
Basic Django website. For learning purposes.

## Deployment
Use following commands to deploy on Linux/Mac OS X system:
```bash
$ cd /usr/projects
$ git clone url
$ virtualenv django-website
$ cd ./django-website
$ source bin/activate
$ pip install -r requirements.txt
$ pip install gunicorn
```

## Running
```bash
$ gunicorn django_website.wsgi -b 0.0.0.0:8001
```