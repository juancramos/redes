import os

os.system("#! /bin/bash")

# Instalación de apache :3 y php5
os.system("echo labredesML340 | sudo apt-get install apache2 -y")
os.system("echo labredesML340 | sudo apt-get install php5 -y")
# Instalación de mysql
os.system("sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password labredesML340'")
os.system("sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password labredesML340'")
os.system("sudo apt-get -y install mysql-server-5.5")

# crear carpeta Downloads
os.system("path = /home/labredes/Downloads")
os.system("if test -d /home/labredes/Downloads")
os.system("then rm -R /home/labredes/Downloads")
os.system("else")
os.system("mkdir /home/labredes/Downloads")
os.system("fi")

#Bajar en Downloady
os.system("wget -P /home/labredes/Downloads http://sourceforge.net/projects/phpscheduleit/files/Booked/2.5/booked-2.5.1.zip")

#Descomprimir :3
os.system("sudo apt-get install unzip")
os.system("mkdir /home/labredes/Downloads/www")
os.system("mkdir /home/labredes/Downloads/www/var")
os.system("cd /home/labredes/Downloads")
os.system("unzip booked-2.5.1.zip -d /home/labredes/Downloads/www/var")
# uishhh que mamera descomprimir

#dar permisos
os.system("cd /home/labredes/Downloads/www/var/booked")
os.system("chmod +x ./tpl")
os.system("chmod +x ./tpl_c")
os.system("chmod +x ./uploads")
#cambiar duenio
os.system("sudo chown www-data ./tpl")
os.system("sudo chown www-data ./tpl_c")
os.system("sudo chown www-data ./uploads")
#copiar a nuevo archivo
os.system("cp ./config/config.dist.php ./config/config.php")
#ocultar archivo .zip
os.system("cd /home/labredes/Downloads")
os.system("cp booked-2.5.1.zip .booked-2.5.1.zip")
os.system("rm booked-2.5.1.zip")
