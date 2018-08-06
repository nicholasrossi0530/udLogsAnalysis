# Database code for the DB Forum, full solution!

import psycopg2, bleach

DBNAME = "news"

def question_1():
  print("Question 1: ")
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select title, count(*) as view_count "+
    "from articles,log "+
    "where path=CONCAT('/article/',slug) "+
    "group by title order by view_count desc limit 3;")
  posts = c.fetchall()
  db.close()
  print(posts)

def question_2():
  print("Question 2: ")
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select authors.name, count(*) as view_count "+
    "from articles,log,authors "+
    "where path=CONCAT('/article/',slug) and author=authors.id "+
    "group by authors.name "+
    "order by view_count desc;")
  posts = c.fetchall()
  db.close()
  print(posts)

def question_3():
  print("Question 3: ")
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select * from"+
    "(SELECT total_date, (100.0*errors/total_views) AS percentage "+
    "FROM"+
    "(SELECT date(time) as total_date, COUNT(*) AS total_views "+
    "FROM log "+
    "GROUP BY date(time) "+
    "ORDER BY date(time)) as total, "+
    "(SELECT date(time) as error_date, COUNT(*) AS errors "+
    "FROM log WHERE status = '404 NOT FOUND' "+
    "GROUP BY date(time) "+
    "ORDER BY date(time)) as error "+
    "WHERE total_date = error_date "+
    "ORDER BY total_date) as percent_table "+
    "where percentage>1;")
  posts = c.fetchall()
  db.close()
  print(posts)

def main():
  question_1()
  question_2()
  question_3()


if __name__ == '__main__':
  main()