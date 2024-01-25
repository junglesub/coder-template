#!/bin/bash

service mariadb start

PASS=$(tr -dc 'A-Za-z0-9!#$%&()*+,-./:;<=>?@[\]^_{|}~' </dev/urandom | head -c 13  ; echo)

mysql -e "set password for 'root'@'localhost'=password('$PASS');"

{
cat <<-EOF >> /usr/share/phpmyadmin/config.inc.php
\$cfg['Servers'][\$i]['auth_type'] = 'config';
\$cfg['Servers'][\$i]['user'] = 'root';
\$cfg['Servers'][\$i]['password'] = '$PASS';
EOF
} 

unset PASS
