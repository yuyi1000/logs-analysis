# Logs Analysis (Overview)

This is an internal reporting tool that connects to local database and provides answers for popular articles and authors of all time. The local database consists of newspaper articles, authors and log. Each time a user browse an article from newspaper website, a row will be added to log table recording information such as article title, author name, network status, etc.

## Database and tables

The name of database for this project is called *news*. It consists of three tables: *articles*, *authors*, and *log*, respectively. Inside the table articles, it keeps records of author name, title, as well as article body, time, etc. Inside the table authors, authors' name and their bio are recorded. For the last table log, it keeps track of web path a user visited, user's ip address, visiting method, status of visiting and timestamp for that visit.

## Available answers

This reporting tool right now is able to answer the following three questions: <br />
1) show popular articles of all time according to their view times <br />
2) show most popular article authors of all time <br />
3) show days that more than 1% requests lead to errors

## How to run

First, download [a file called newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) in a Linux machine, then install [PostgreSQL](https://www.postgresql.org/) and run command
`psql -d news -f newsdata.sql`
which creates a new database called news and three tables called articles, authors, and log, respectively.
Finally, run
`python3 newsdata.py` and you will get the result for popular articles and authors from news website.
