# django-website
Basic Django website. For learning purposes.

## Deployment
Use following commands to deploy on Linux/Mac OS X system:
```bash
$ cd /usr/projects
$ git clone https://github.com/hazadus/django-website
$ virtualenv django-website
$ cd ./django-website
$ source bin/activate
$ pip install -r requirements.txt
$ pip install gunicorn
```

## Running
Edit `nginx` config `/etc/nginx/conf.d/virtual.conf`:
```
server {
    server_name  hazadus.ru www.hazadus.ru;
    
    location /django/ {
        proxy_pass http://127.0.0.1:8001/;
    }
}
```
Then run gunicorn:
```bash
$ cd /usr/projects/django-website
$ source bin/activate
$ gunicorn django_website.wsgi -b 0.0.0.0:8001 &
```

## References
- [Django Documentation](https://docs.djangoproject.com/en/4.1/)
- [CodeMy Django Wednesdays Series](https://www.youtube.com/playlist?list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy)
- [How to use Django with Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/)