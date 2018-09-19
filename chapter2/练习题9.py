# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser()
config.read('my.cnf')

# config.set('mysqld','default-time-zone','+00:00')
# config.write(open('my.cnf', "w"))

# config.remove_option('mysqld','explicit_defaults_for_timestamp')
# config.write(open('my.cnf', "w"))
config.set('DEFAULT','haracter-set-server' , 'utf8')
config.write(open('my.cnf', "w"))


