#!/bin/bash
clear
sudo docker-compose down
sudo docker-compose up -d
sudo docker-compose ps
