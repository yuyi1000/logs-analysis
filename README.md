# Logs Analysis

This is an internal reporting tool that connects to local database and provides answers for popular articles and authors of all time. The local database consists of newspaper articles, authors and log. Each time a user browse an article from newspaper website, a row will be added to log table recording information such as article title, author name, network status, etc.



## How to run

First, download [a file called newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) in a Linux machine, then install [PostgreSQL](https://www.postgresql.org/) and run command
`psql -d news -f newsdata.sql`
which creates a new database called news and three tables called articles, authors, and log, respectively.
Finally, run
`python3 newsdata.py` and you will get the result for popular articles and authors from news website.
