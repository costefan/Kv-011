#!/bin/bash

#vagrant ssh
source Kv-011/env/bin/activate
pip3 install -r /vagrant/SSP/requirements.txt
python3 /vagrant/SSP/manage.py makemigrations
python3 /vagrant/SSP/manage.py migrate
