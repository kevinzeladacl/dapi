#!/bin/bash
clear
cat << "EOF"

              _                            _              _             _          _____ 
             | |                          | |            | |           (_)        / __  \
__      _____| | ___ ___  _ __ ___   ___  | |_ ___     __| | __ _ _ __  _  __   __`' / /'
\ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \   / _` |/ _` | '_ \| | \ \ / /  / /  
 \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | (_| | (_| | |_) | |  \ V / ./ /___
  \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__,_|\__,_| .__/|_|   \_/  \_____/
                                                                 | |                     
                                                                 |_|     for appactory.cl
                                                                         by  @kevinzeladacl   

==========================================================================================

SELECT A OPTION (enter number):


0 - RUN WITH DEBUG CONSOLE (DEV)
1 - RUN WITH DEBUG CONSOLE (PROD)
2 - AUTO LOCAL MIGRATIONS
3 - AUTO PROD MIGRATIONS
4 - CREATE SUPER USER
999 - INSTALL PROJECT LOCAL

===========================================================================================

EOF

read opcion
case $opcion in
  999) 
     echo "Instando ..."
     pip install -r requirements/initial.txt
     python3 manage.py makemigrations --settings=dapi.settings.local
     python3 manage.py migrate --settings=dapi.settings.local
  ;;
  0) 
	 echo "RUN WITH DEBUG CONSOLE (DEV)..."
     python3 manage.py runserver 0.0.0.0:8000 --settings=dapi.settings.local
  ;;
  1) 
   echo "RUN WITH DEBUG CONSOLE (PROD)..."
     python3 manage.py runserver 0.0.0.0:8000 --settings=dapi.settings.prod
  ;;
  2)
     echo "RUN AUTO LOCAL MIGRATIONS..."
     pip install -r requirements/initial.txt
     python3 manage.py makemigrations --settings=dapi.settings.local
     python3 manage.py migrate --settings=dapi.settings.local
  ;;
  3)
     echo "RUN AUTO PROD MIGRATIONS..."
     pip install -r requirements/initial.txt
     python3 manage.py makemigrations --settings=dapi.settings.prod
     python3 manage.py migrate --settings=dapi.settings.prod
  ;;
  4) 
   echo "CREATE SUPER USER..."
     python3 manage.py createsuperuser --settings=dapi.settings.local
  ;;
  *)
     echo "Select a valid option 77"
  ;;

esac