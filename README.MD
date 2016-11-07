#Deprivation map

#Installation
`git clone https://github.com/TileStache/TileStache.git`  
`cd TileStache`  
`sudo python setup.py install`  
`sudo apt-get install redis-server apache2 libapache2-mod-python`  
`sudo pip install redis mapnik`  

#Config
Copy example_apache2.conf to /etc/apache2/sites-enabled and make edits where appropriate  
`sudo apache2 reload`  