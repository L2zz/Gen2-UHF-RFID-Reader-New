#! /bin/sh

#sudo sysctl -w net.core.rmem_max=50000000
#sudo sysctl -w net.core.wmem_max=1048576
#sudo GR_SCHEDULER=STS nice -n -20 

rm -f debug_message
rm -f time/time
sudo python reader.py
sudo python make_csv.py develop_50
rm -f why
