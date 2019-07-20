import psycopg2
import datetime
DBNAME = "news"


# querying the database for the most popular three articles of all time
def mostPopularArticles():
    print("\nThe most popular three articles of all time:\n")
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(
        "SELECT articles.title, count(log.id) AS Views "
        "FROM log, articles "
        "WHERE log.path LIKE '%article%' "
        "AND (substring(log.path FROM 10) = articles.slug) "
        "GROUP BY articles.title "
        "ORDER BY Views DESC LIMIT 3")
    results = cursor.fetchall()
    for row in results:
        print(row[0] + " --- " + str(row[1]) + " Views")

    cursor.close()
    db.close()

def mostPopularAuthors():
    print("\nThe most popular authors of all time:\n")
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(
        "SELECT authors.name, count(log.id) AS Views "
        "FROM log, articles,authors "
        "WHERE log.path LIKE '%article%' "
        "AND (substring(log.path FROM 10) = articles.slug) "
        "AND (articles.author= authors.id) "
        "GROUP BY authors.name "
        "ORDER BY Views DESC")
    results = cursor.fetchall()
    for row in results:
        print(row[0] + " --- " + str(row[1]) + " Views")

    cursor.close()
    db.close()

def highErrorDays():
    print("\nexi:\n")
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(
        "SELECT DATE(log.time), "
        "trunc(AVG(CASE WHEN log.status LIKE '4%' OR log.status LIKE '5%' THEN 1 ELSE 0 END)::DECIMAL*100,2) "
        "FROM log "
        "GROUP BY DATE(log.time) "
        "HAVING AVG(CASE WHEN log.status LIKE '4%' or log.status LIKE '5%' THEN 1 ELSE 0 END)>0.01 ")
    results = cursor.fetchall()
    for row in results:
        dt = row[0]
        percentage = row[1]
        print(dt.strftime("%b %d %Y")+" --- "+str(percentage)+"%")

    cursor.close()
    db.close()

