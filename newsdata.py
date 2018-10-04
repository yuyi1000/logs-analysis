import psycopg2

'''
show most popular three articles of all time
'''
def get_top_three_articles ():
    pass

'''
show most popular article authors of all time
'''
def get_authors_rank ():
    pass


'''
show days that more than 1% requests lead to errors
'''
def get_high_request_error_days ():
    pass



def _show_results (description, results):
    widths = []
    columns = []
    tavnit = '|'
    separator = '+'

    for cd in description:
        widths.append(max(cd[2], len(cd[0])))
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
