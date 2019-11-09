#!/bin/bash

git clone https://github.com/datacharmer/test_db.git /tmp/test_db \
    && cd /tmp/test_db \
    && mysql -u root -p$MYSQL_ROOT_PASSWORD < employees.sql \
    && mysql -t -u root -p$MYSQL_ROOT_PASSWORD < test_employees_md5.sql \
    && git clone https://github.com/dalers/mywind.git /tmp/mywind \
    && cd /tmp/mywind \
    && mysql -u root -p$MYSQL_ROOT_PASSWORD < northwind.sql \
    && mysql -u root -p$MYSQL_ROOT_PASSWORD < northwind-data.sql \
    && /usr/bin/mysqladmin -u root -p$MYSQL_ROOT_PASSWORD stop