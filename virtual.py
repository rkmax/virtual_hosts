#!/usr/bin/python

from optparse import OptionParser
import os

parser = OptionParser()
path_apache_vhost = '/etc/apache2/sites-available/{0}'
path_sys_hosts = '/etc/hosts'

parser.add_option( "-d", "--directory", dest="directory", help="The path to the directory", metavar="DIRECTORY" )
parser.add_option( "-n", "--name", dest="name", help="Name of the virtual host", metavar="NAME" )

(options, args) = parser.parse_args()

template_dir_path = os.path.join(os.path.dirname(__file__), 'template')

template = open( template_dir_path, 'r' )
virtualHostText = template.read()
template.close()



# leer el archivo host
fileHosts = open(path_sys_hosts, 'r')
text_host = fileHosts.read();
fileHosts.close()

# comprueba que no exista la entrada en el archivo host
if text_host.find("{0}".format(options.name)) < 0:
  fileHosts = open(path_sys_hosts, 'a')
  fileHosts.write("127.0.0.1 {0}\n".format(options.name))
  fileHosts.close()

virtualHostText = virtualHostText.format( name = options.name,  directory = options.directory )

fileNameVirtualHost = path_apache_vhost.format(options.name)
fileNameVirtualHost = '/etc/apache2/sites-available/{0}'.format(options.name)
fileVirtualHost = open( fileNameVirtualHost, 'w' )
fileVirtualHost.write( virtualHostText )
fileVirtualHost.close()

# activa el nuevo stio y reinicia apache2
os.system('a2ensite {0}'.format(options.name))
os.system('service apache2 restart')

