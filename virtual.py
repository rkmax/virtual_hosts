#!/usr/bin/python3

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

fileNameVirtualHost = '/etc/apache2/sites-available/{0}.conf'.format(options.name)
fileVirtualHost = open( fileNameVirtualHost, 'w' )
fileVirtualHost.write( virtualHostText )
fileVirtualHost.close()

os.symlink( fileNameVirtualHost, '/etc/apache2/sites-enabled/{0}.conf'.format(options.name) )

os.system('/etc/init.d/apache2 restart')
