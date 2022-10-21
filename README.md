# django-website
Basic Django website. For learning purposes.

## Future improvements
**High priority**
- ~~Add profile page.~~
- Add user address, telegram id to profile.
- Use static files - images, etc.

**Medium priority**
- ~~Add image uploads.~~
- Add multiple images for one DB Model (eg product photos).
- Email/Telegram notifications.

**Low priority**
- Use email for logging in.
- Restore lost password.
- Verify email when registering.
- Built-in JS for product form-filling from Discogs API.
- Product categories (aka breadcrumbs) for shop.
- Add Sentry.io watchdog.
- Try with real db like MySQL.

## Deploying on Linux system using nginx/gunicorn
Use following commands to deploy on Linux system:
```bash
$ cd ~/projects
$ git clone https://github.com/hazadus/django-website
$ virtualenv django-website
$ cd ./django-website
$ source bin/activate
$ pip install -r requirements.txt
$ pip install gunicorn
```
Install `nginx` if it is not already on your system. Config `ufw` to allow `nginx` if you use `ufw`:
```bash
$ sudo apt install nginx
$ sudo ufw allow 'Nginx Full'
$ sudo ufw allow 'Nginx HTTP'
$ sudo ufw allow 'Nginx HTTPS'
```
Edit `nginx` config `/etc/nginx/conf.d/virtual.conf`:
```
server {
    server_name yoursitename.com www.yoursitename.com;
    
    location / {
        proxy_pass http://127.0.0.1:8001/;
    }
}
```
If you don't have any domain name yet, just use your server's IP as `server_name` in the config above.

Check `nginx` config file, then restart `nginx` service:
```bash
$ sudo nginx -t
$ sudo service nginx restart
```

## Starting and restarting server
### On first run
Make DB migrations:
```bash
$ ./manage.py makemigrations
$ ./manage.py migrate
```
Create admin account:
```bash
$ ./django-admin createsuperuser
```
If you're using **SQLite3** database for your project, you can simply copy `db.sqlite3` file from your local Mac to
remote server with following command  (assuming you're in projects directory, type it in your local terminal,
not in remote SSH connection):
```bash
$ scp ./db.sqlite3 username@1.2.3.4:~/projects/django-website/
```
### Starting server
**To run locally** in development environment:
```bash
$ export DJANGO_SECRET="django-insecure-secret-code-goes-here-****************"
$ export DJANGO_DEBUG=1
$ cd ~/projects/django-website
$ source bin/activate
$ ./manage.py runserver
```

**Server mode**: run `gunicorn` using following commands.
You can save these commands to bash script file, say `run_bot.sh`, just don't forget to make it executable with
`chmod a+x run_bot.sh`. Next time, you can run your Django site by typing `run_bot.sh`, assuming you're in
projects directory. 
```bash
$ export DJANGO_SECRET="django-insecure-secret-code-goes-here-****************"
$ export DJANGO_DEBUG=1
$ cd ~/projects/django-website
$ source bin/activate
$ gunicorn django_website.wsgi -b 0.0.0.0:8001 &
```
Now you should be able to see the app working, by pointing your browser to `http://www.yoursitename.com`.

### Restarting server
To kill `gunicorn` server, you need to find it's process id first, then use `kill` command, like this (change PID to
actual proccess ID found by first command):
```bash
$ ps ax | grep gunicorn
$ kill -9 PID
```
After killing `gunicorn`'s process, follow instructions from section above to start it agagin.

There's also a way to restart `gunicorn` with just one command line (replace `django-website` wuth your actual project
folder name):
```bash
ps aux | grep gunicorn | grep django-website | awk '{ print $2 }' | xargs kill -HUP
```
This command parses gunicorn PIDs from `ps aux` output, then executes `kill -HUP` on each PID. `gunicorn` restars when
HUP signal is received ([read more on this here](https://docs.gunicorn.org/en/latest/signals.html#reload-the-configuration)).

## References
- [Django Documentation](https://docs.djangoproject.com/en/4.1/)
- [Widgets - Django Documentation](https://docs.djangoproject.com/en/4.1/ref/forms/widgets/)
- [CodeMy Django Wednesdays Series](https://www.youtube.com/playlist?list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy)
- [How to use Django with Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/)
- [Gunicorn Signal Handling](https://docs.gunicorn.org/en/latest/signals.html#reload-the-configuration)
- [ReportLab User's Guide](https://www.reportlab.com/docs/reportlab-userguide.pdf)