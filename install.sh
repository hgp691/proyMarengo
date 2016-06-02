#instalacion de archivos

#creacion de las carpetas en usb que guardan los datos
sudo mkdir /mnt/usb/config/
sudo mkdir /mnt/usb/datos/
sudo mkdir /mnt/usb/logs/

#instalar requests
cd /mnt/usb/ && git clone git://github.com/kennethreitz/requests.git
cd /mnt/usb/requests/ && sudo python setup.py install -y

#copiar los archivos de inicio
sudo cp /etc/rc.local /etc/rc.local.bup
sudo rm /etc/rc.local
sudo cp /sistema/rc.local /etc/rc.local

sudo cp /etc/crontab /etc/crontab.bup
sudo rm /etc/crontab
sudo cp /sistema/crontab /etc/crontab

#copiar los archivos de configuracion
sudo cp /sistema/config/* /mnt/usb/config/ -r