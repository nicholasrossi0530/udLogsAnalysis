Navigate to the location of vagrant.
Run vagrant up.
Run vagrant ssh.
Navigate to /vagrant and then to where the database data is located.
Run psql -d news -f newsdata.sql to load the data into the database.
Run python newsdata.py to get the output text.