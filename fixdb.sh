#!/bin/zsh

root_dir=`pwd`
current_dir=`pwd`
if [ $root_dir = $current_dir ]
then
source .env/bin/activate
./manage.py makemigrations ; ./manage.py migrate
echo 'DONE'
else 
echo 'Wrong Dir, exiting...'
fi
