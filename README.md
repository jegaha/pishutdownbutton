# Pi Shutdown Button
This package will install a small Python script wich runs to listen for a GPIO signal to start a shutdown sequence.
Shutdown steps can be defined in form of multiple *.sh scripts inside /usr/local/bin/pishutdownbutton.d/ directory.

## build package

    native:# dpkg-deb --build pishutdownbutton_1.0-2
    docker:# docker run -it -v $PWD:/mnt --workdir /mnt debian dpkg-deb --build pishutdownbutton_1.0-2

## install package

sudo dpkg -i pishutdownbutton_1.0-2.deb

## start/stop Service
    systemctl start pishutdownbutton
    systemctl stop pishutdownbutton
