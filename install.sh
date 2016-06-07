#instalacion de archivos

#creacion de las carpetas en usb que guardan los datos
sudo mkdir /mnt/usb
sudo mount /dev/sda1/ /mnt/usb/
sudo mkdir /mnt/usb/config/
sudo mkdir /mnt/usb/datos/
sudo mkdir /mnt/usb/logs/

#instalar requests
sudo apt-get install python-pip -y
sudo pip install requests

#instalar libreria DHT11
sudo apt-get install python-dev -y
cd /mnt/usb/ && sudo git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd /mnt/usb/Adafruit_Python_DHT && sudo python setup.py install

#copiar los archivos de inicio
sudo cp /etc/rc.local /etc/rc.local.bup
sudo rm /etc/rc.local
sudo cp /var/proyMarengo/sistema/rc.local /etc/rc.local

sudo cp /etc/crontab /etc/crontab.bup
sudo rm /etc/crontab
sudo cp /var/proyMarengo/sistema/crontab /etc/crontab

#copiar los archivos de configuracion
sudo cp /var/proyMarengo/sistema/config/* /mnt/usb/config/ -r

#eliminar lo que no se usa en proyMarengo
sudo rm /var/proyMarengo/sistema -r

#ejecutar configuracion gráfica
sudo apt-get install python-tk -y