# Hive Queries
You can use the cloudera to install the HDFS and make use of Apache Ambari to test the Hive file system.
The Hive  as a data warehousing service, in the high level, has a sql abstraction, and you can simply write queries like relational databases.
The Hive provides this abstraction for MapReduce apps. 

These are some sample queires in Hive:
```sql
CREATE VIEW IF NOT EXISTS topratingmovies AS
SELECT movie_id, count(movie_id) AS topratings
FROM ratings
GROUP BY movie_id
ORDER BY topratings DESC;
SELECT n.title, topratings FROM topratingmovies t JOIN names n ON t.movie_id = n.movieid;
```

```sql
CREATE VIEW IF NOT EXISTS AVGratings AS
SELECT movie_id, COUNT(movie_id) AS totalRatings, AVG(rating) AS avgRatings
FROM ratings
GROUP BY movie_id
ORDER BY avgRatings DESC;
SELECT n.title, avgratings FROM AVGratings a JOIN names n ON n.movieid = a.movie_id WHERE a.totalratings > 10;
```