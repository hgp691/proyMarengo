#instalacion de archivos

#creacion de las carpetas en usb que guardan los datos
sudo mkdir /mnt/usb/config/
sudo mkdir /mnt/usb/datos/
sudo mkdir /mnt/usb/logs/

#instalar requests
cd /mnt/usb/ && git clone git://github.com/kennethreitz/requests.git
cd /mnt/usb/requests/ && sudo python setup.py install -y

#copiar los archivos de inicio
