import psycopg2

'''
show popular articles of all time according to their view times
'''
def get_top_three_articles ():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute("select title, views from articles, \
                    (select path, count(*) as views from log group by path order by views desc) as rank \
                    where path like '%' || slug")
    results = cursor.fetchall()
    db.close()
    _show_results(cursor.description, results)

'''
show most popular article authors of all time
'''
def get_authors_rank ():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute("select name, sum(count) as views from articles, authors, \
                    (select path, count(*) from log group by path order by count desc) as rank \
                    where path like '%' || slug and authors.id = author group by authors.id")
    results = cursor.fetchall()
    db.close()
    _show_results(cursor.description, results)


'''
show days that more than 1% requests lead to errors
'''
def get_high_request_error_days ():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute("select total.time, error.count / total.count::real as error_rate \
                    from (select time::date, count(*) from log group by time::date) as total, \
                    (select time::date,  count(*) from log where status = '404 NOT FOUND' \
                    group by time::date order by time::date) as error \
                    where total.time = error.time and error.count / total.count::real > 0.01")
    results = cursor.fetchall()
    db.close()
    _show_results(cursor.description, results)


def _show_results (description, results):
    widths = []
    columns = []
    tavnit = '|'
    separator = '+'

    for index, cd in enumerate(description):
        # widths.append(max(cd[2], len(cd[0])))
        widths.append(max(max([len(str(result[index])) for result in results]), len(cd[0])))
        columns.append(cd[0])

    for w in widths:
        tavnit += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in results:
        print(tavnit % row)
    print(separator)

if __name__ == '__main__':
    get_top_three_articles()
    get_authors_rank()
    get_high_request_error_days()
