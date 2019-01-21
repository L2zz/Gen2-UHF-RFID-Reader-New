#! /bin/sh

#sudo sysctl -w net.core.rmem_max=50000000
#sudo sysctl -w net.core.wmem_max=1048576
#sudo GR_SCHEDULER=STS nice -n -20 

sudo python reader.py
sudo python make_csv.py modi1
rm -f why
