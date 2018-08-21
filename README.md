This tool analyzes a database of newspaper articles and web server logs and answers these 3 questions: 
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

To run this tool, follow these instructions:
Navigate to the location of vagrant.
Run vagrant up.
Run vagrant ssh.
Navigate to /vagrant and then to where the database data is located.
Run psql -d news -f newsdata.sql to load the data into the database.
Run python newsdata.py to get the output text.