import psycopg2


def get_top_three_articles ():
    pass

def get_authors_rank ():
    pass

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
