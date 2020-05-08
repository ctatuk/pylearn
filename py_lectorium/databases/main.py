import sys
import psycopg2
import base64

def main(auth):
    user, pwd = base64.b64decode(auth).decode('ascii').split(':')
    conn = None
    try:
        conn = psycopg2.connect(
            "dbname='sample' user='%s' host='sql-test-postgres.cfdqnys76xyr.us-east-1.rds.amazonaws.com' password='%s'" % (user, pwd))
    except:
        print("I am unable to connect to the database")
    if conn:
        cur = conn.cursor()
        # SQL
        cur.execute("""select 
        substring(author from 1 for 1), avg(page_count) 
        from books
        group by substring(author from 1 for 1)
        having count(*) >1
        order by substring(author from 1 for 1)
        """)
        print(cur.fetchall())
        cur.close()
        conn.commit()
        conn.close()

def insert_books(cur):
    book_list = """War and Peace, Tolstoy, 2018, 1472
            12 chairs, Ilf&Petrov, 2011, 608
            3 Musketeers, Dima, 2012, 640
            Treasure Island, Stevenson, 2013, 448
            Gulliver's travels, Swift, 2018, 192
            “Baron Munchausens Narrative of his Marvellous Travels and Campaigns in Russia”, Raspe, 2017, 192
            “Harry Potter and the Philosopher's stone”, Rowling, 1997, 223
            “Comet in Moominland”, Jansson, 1951, 214
            “Myths of the Ancient Greeks”, Martin, 2003, 346
            “Baron Munchausens Narrative of his Marvellous Travels and Campaigns in Russia”, Martin, 2003, 192"""
    book_list_parsed = book_list.split('\n')
    for num, book in enumerate(book_list_parsed):
        attrs = book.strip().split(', ')
        sql = """insert into books(book_id, title, author, publish_year, page_count) values({}, '{}', '{}', {}, {})""".format(
            num + 2, attrs[0].replace("'", ""), attrs[1], attrs[2], attrs[3])
        cur.execute(sql)

def insert_visitors(cur):
    visitor_list = """Vasin Eugene, Shariokvaya 13, 1965, evasin@mail.ru
    Shavygina Svetlana, Kirovskaya 21, 1978, sshavygina@mail.ru
    Eremeev Sergey, Kahovka 13, 2001, seremeev@mail.ru"""
    visitor_list_parsed = visitor_list.split('\n')
    for num, visitor in enumerate(visitor_list_parsed):
        attrs = visitor.strip().split(', ')
        sql = """insert into visitors(visitor_id, name, address, birth_year, email) values({}, '{}', '{}', {}, '{}')""".format(
            num + 1, attrs[0], attrs[1], attrs[2], attrs[3])
        cur.execute(sql)

def insert_loans(cur):
    loan_list = """1, 3, september 5th 2020, september 29th 2020
    3, 1, june 10th 2020, june 16th 2020"""
    loan_list_parsed = loan_list.split('\n')
    for num, loan in enumerate(loan_list_parsed):
        attrs = loan.strip().split(', ')
        sql = """insert into loan_books(visitor_id, book_id, loan_start, loan_end) values({}, {}, '{}', '{}')""".format(
            attrs[0], attrs[1], attrs[2], attrs[3])
        cur.execute(sql)

def create_loan_books(cur):
    cur.execute("""create table loan_books (
            visitor_id int,
            book_id int,
            loan_start varchar(20),
            loan_end varchar(20)
            )
            """)

if __name__ == '__main__':
    main(str(sys.argv[1]))