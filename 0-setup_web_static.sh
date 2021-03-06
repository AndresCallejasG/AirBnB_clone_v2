#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
apt-get -y update
sudo apt-get -y install nginx
mkdir /data/ /data/web_static/ /data/web_static/releases/
mkdir /data/web_static/shared/ /data/web_static/releases/test/
echo -e "<html>
  <head>
    <title>AirBnb Clone</title>
  </head>
  <body>
    AirBnB Clone - Web Static
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i '20i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
