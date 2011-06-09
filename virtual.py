#!/usr/bin/python

from optparse import OptionParser
import os

parser = OptionParser()

parser.add_option( "-d", "--directory", dest="directory", help="The path to the directory", metavar="DIRECTORY" )

parser.add_option( "-n", "--name", dest="name", help="Name of the virtual host", metavar="NAME" )

(options, args) = parser.parse_args()

template = open( 'template', 'r' )
virtualHostText = template.read()
template.close()

virtualHostText = virtualHostText.format( name = options.name, directory = options.directory )

fileNameVirtualHost = '/etc/apache2/sites-available/{0}'.format(options.name)
fileVirtualHost = open( fileNameVirtualHost, 'w' )
fileVirtualHost.write( virtualHostText )
fileVirtualHost.close()


fileNameSystemHost = '/etc/hosts'
fileSystemHost = open( fileNameSystemHost, 'a' )
fileSystemHost.write( '127.0.0.1  {0}'.format(options.name))
fileSystemHost.close()

os.system('a2ensite {0}'.format(options.name))
os.system('/etc/init.d/apache2 restart')
