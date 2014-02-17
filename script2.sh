#! /bin/bash

# Instalación de apache :3 y php5
echo labredesML340 | sudo apt-get install apache2 -y
echo labredesML340 | sudo apt-get install php5 -y
# Instalación de mysql
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password labredesML340'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password labredesML340'
sudo apt-get -y install mysql-server-5.5

# crear carpeta Downloads
path = /home/labredes/Downloads
if test -d /home/labredes/Downloads
then rm -R /home/labredes/Downloads
else
mkdir /home/labredes/Downloads
fi

#Bajar en Downloady
wget -P /home/labredes/Downloads "http://sourceforge.net/projects/phpscheduleit/files/Booked/2.5/booked-2.5.1.zip"

#Descomprimir :3
sudo apt-get install unzip
mkdir /home/labredes/Downloads/www
mkdir /home/labredes/Downloads/www/var
cd /home/labredes/Downloads
unzip booked-2.5.1.zip -d /home/labredes/Downloads/www/var
# uishhh que mamera descomprimir

#dar permisos
cd /home/labredes/Downloads/www/var/booked
chmod +x ./tpl
chmod +x ./tpl_c
chmod +x ./uploads
#cambiar duenio
sudo chown www-data ./tpl
sudo chown www-data ./tpl_c
sudo chown www-data ./uploads
#copiar a nuevo archivo
cp ./config/config.dist.php ./config/config.php
#ocultar archivo .zip
cd /home/labredes/Downloads
cp booked-2.5.1.zip .booked-2.5.1.zip
rm booked-2.5.1.zip
