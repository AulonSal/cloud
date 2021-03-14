[[Backups]] Backups.md# Notes
### Miscellaneous
- Client request bufferred is not a problem
#### Secret key
```
from django.core.management.utils import get_random_secret_key 
get_random_secret_key()  
```
### Database migration 
https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn
https://docs.djangoproject.com/en/3.0/ref/databases/#postgresql-notes
https://www.shubhamdipt.com/blog/django-transfer-data-from-sqlite-to-another-database/

### Forms
- You have to make a field blank=true for form validation if you make it null=True, otherwise though the db allows null, the form won't allow blank.

### Installation
#### Nginx + ~~Daphne~~
User http this time though
https://wiki.archlinux.org/index.php/Nginx
https://medium.com/@Ritiktaneja/configuring-asgi-django-application-using-daphne-and-nginx-server-59a90456fe17
Still needed to own overything
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-centos-7
The way it works right now is that it sends everything on root to daphne on localhost:9001
And for the same, it makes alll calls to static, prod_static
https://www.nginx.com/blog/creating-nginx-rewrite-rules/#rerouting
Sends /static/ to /prod_static/ https://stackoverflow.com/questions/6711971/regular-expressions-match-anything
Enabled tls1.3 and http2 and god knows what, installed twisted, http2
Redirecting http to https
https://phoenixnap.com/kb/redirect-http-to-https-nginx
***
#### Switched to hypercorn

#### Systemd config
Arch runs nginx under user http by default
We add http to group ccs, and then run hypercorn under group http, just for ease of understanding I think, because group ccs also actually works, as the gorup should be able to read and write, and the group can since http is in group ccs.
```
[Unit]  
Description=ASGI application-server instance to serve ccs-website-django  
After=network.target  
  
[Service]  
User=ccs  
Group=http  
WorkingDirectory=/home/ccs/ccs-website-django/website  
ExecStart=poetry run hypercorn --bind unix:ccs-web.sock --workers 3 -m 007 ccs_django.asgi:application  
  
[Install]  
WantedBy=multi-user.target
```

### Oembed
Oembed documentation: https://oembed.com/
Wagtail: https://github.com/wagtail/wagtail/blob/master/wagtail/embeds/oembed_providers.py
Use this: https://github.com/wagtail/wagtail/issues/5381 
Always look at oembed.com, not provider docs
The repl.it documentation is garbage, had to configure it while stumbling.

### Live setup
- Download pem key, use it to sign in as arch
- Create user ccs of group wheel, with home dir,
- Update, add poetry, base-devel, ranger, neovim, vi, git, postgresql, nginx-mainline, nmap, man-db, man-pages, texinfo, tree, ripgrep
- Update timezone and locale(was correct this time), lang (still wrong)
- Add password to ccs
- Use visudo to give wheel sudo access
- Copy .ssh folder from arch to ccs, add own keys
- Reboot, chown and chgrp .ssh and the files within
- Optionally, edit client ssh file with hostname, user etc.
- Copy reduced bashrc (Ranger + Poetry + other stuff) and gitconfig
- Copy ssh deploy key
- git clone
- poetinst
- copy nginx config and ccs-web systemd service unit file, replacing https and http/2 with the normal http thing right now so port 80
- Copy the website config over
- Create database in the same vpc as server, keep different secuirty group
- Open database security group to inbound psql from vps security group and my ip
- Load database into db server, with \i
- Do database setup from client
- Setup ngingx non-https
- Add user http to group ccs, chmod /home/ccs 710, btw, ssh doesn't work if the home directory is writeable by anybody other than the user, even the 
- Ensure allowed hosts
- Run migrations
- Run pyma collectstatic
- Point website at it
- Get certbot and certbot-nginx
- Get the ssl cert for placements.ccstiet.com, 
- Replace with the ssl nginx config, but with https managed by certbot

##### Bringing the other app online
Clone the deployment folder
Copy the correct nginx config
Copy the placements systemd service - This is also where the environment variable is to be set https://coreos.com/os/docs/latest/using-environment-variables-in-systemd-units.html
Reboot
Start and enable the placements systemd service
Daemon reload
Start and enable nginx

###### Choices made:
I did not hardcode the location of the json, as I don't know why it was left like that
I did not commit the poetry files
Choosing to not set the env var in /etc/profile.d for purely test purposes
3 workers

##### Ran script using https://realpython.com/run-python-scripts/
Had to change basedir in it though

##### Final stuff certbot
Installed certbot, certbot-nginx, cronie for cron

##### dnsmasq
https://aws.amazon.com/premiumsupport/knowledge-center/dns-resolution-failures-ec2-linux/
F this, follow arch, but use part of this config
Had to allow externally getting to this ip otherwise it wasn't working
for the sec group access
Follow theirconfig, but remove resolv file, add no-resolve, mention all servers, in resolv.conf put ::1 and 127.0.0.1 and then sticky bit on it.
Remove symlink on resolv.conf before this.

#### Disqus
https://help.disqus.com/en/articles/1717301-i-m-receiving-the-message-we-were-unable-to-load-disqus
All that you need to do^

### Fixing migrations
Check out fake migrations, and applying them. 

