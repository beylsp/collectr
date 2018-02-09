from rq import Queue
from scraper import crawl
from worker import conn

q = Queue(connection=conn)


if __name__ == '__main__':
    result = q.enqueue(crawl)
