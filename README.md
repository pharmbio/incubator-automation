# DYO incubator-automation

## Setup and test CLI
```
cd python-version
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt

# Add rules to allow reading usb device
sudo cp 50-incubator-actuator.rules /etc/udev/rules.d/

# Make sure user belongs to dialout group
sudo usermod -a -G dialout $USER


python test_incubator.py reset
python test_incubator.py set 100
python test_incubator.py get

# Not needed (default is max speed)
python test_incubator.py speed 1023

# Not needed (default 4, is OK)
python test_incubator.py acuracy 10

```
