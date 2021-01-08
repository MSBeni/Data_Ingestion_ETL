# In this repository we will focus on the postgres and simple to professional use cases

_ First install postgress on your system using this link: 
https://www.postgresql.org/download/
check the version simply on your linux terminal: 
```bash
$ psql --version
```
- It is always easier to use the docker container to install the postgres and the related GUI which is pgAdmin.
Please check this repository to do so: https://gist.github.com/jkatz/98dc5d614fbbfbd2b80b65a7f4561996
```bash
$ mkdir postgres
$ cd postgres

$ docker volume create --driver local --name=pgvolume
$ docker volume create --driver local --name=pga4volume

$ docker network create --driver bridge pgnetwork

$ cat << EOF > pg-env.list
PG_MODE=primary
PG_PRIMARY_USER=postgres
PG_PRIMARY_PASSWORD=yoursecurepassword
PG_DATABASE=testdb
PG_USER=yourusername
PG_PASSWORD=yoursecurepassword
PG_ROOT_PASSWORD=yoursecurepassword
PG_PRIMARY_PORT=5432
EOF

$ cat << EOF > pgadmin-env.list
PGADMIN_SETUP_EMAIL=youremail@yourdomain.com
PGADMIN_SETUP_PASSWORD=yoursecurepassword
SERVER_PORT=5050
EOF

$ docker run --publish 5432:5432 \
  --volume=pgvolume:/pgdata \
  --env-file=pg-env.list \
  --name="postgres" \
  --hostname="postgres" \
  --network="pgnetwork" \
  --detach \
crunchydata/crunchy-postgres:centos7-10.9-2.4.1

$ docker run --publish 5050:5050 \
  --volume=pga4volume:/var/lib/pgadmin \
  --env-file=pgadmin-env.list \
  --name="pgadmin4" \
  --hostname="pgadmin4" \
  --network="pgnetwork" \
  --detach \
crunchydata/crunchy-pgadmin4:centos7-10.9-2.4.1
```
Then 2.  Do the following in your web browser:
- Go to http://localhost:5050/
- Log into pgAdmin 4 with
    - Email: youremail@yourdomain.com
    - Password: yoursecurepassword
- Add a server using:
    - Hostname: postgres
    - Username: yourusername
    - Password: yourpassword
    
You can always use the the .sql files in the sql_database folder to query to build some test tables.
The most standard queries will be reviewed here:
- SELECT:
```bash
SELECT items.name AS "items name", items.price FROM items;
``` 
- Filtering with WHERE:
```bash
SELECT items.name AS "items name", items.price FROM items WHERE items.price > 10;
``` 
```bash
SELECT customers.id FROM customers WHERE customers.first_name = 'Rolf' OR customers.last_name = 'Watson';
``` 
- LIMIT for limiting the number of results:
```bash
SELECT customers.first_name, customers.id FROM customers WHERE customers.first_name = 'Rolf' OR customers.last_name = 'Watson' LIMIT 1;
``` 
- UPDATE data in a table:
```bash
UPDATE items SET price=10 WHERE items.price < 10;
``` 
- DELETE data from a table:
```bash
DELETE FROM purchaces WHERE items.id=4;
``` 
- LIKE SQL Wildcards for filtering unknowns:
```bash
SELECT * FROM customers WHERE last_name LIKE '%t%'; 
``` 
- JOIN:

INNER JOIN, LEFT JOIN, RIGHT JOIN and FULL JOIN:
```bash
SELECT * FROM customers INNER JOIN purchases ON customers.id = purchases.customer_id; 
``` 

- GROUP BY:
```bash
SELECT customers.first_name, customers.last_name, COUNT(purchases.id) FROM customers INNER JOIN purchases ON customers.id = purchases.customer_id GROUP BY customers.id;  
``` 
```bash
SELECT customers.last_name, customers.first_name, SUM(items.price) FROM items
INNER JOIN purchases ON items.id = purchases.item_id
INNER JOIN customers ON purchases.customer_id = customers.id
GROUP BY customers.id;
``` 

- ORDER BY for sorting data:
```bash
SELECT customers.last_name, customers.first_name, SUM(items.price) AS "total spent" FROM items
INNER JOIN purchases ON items.id = purchases.item_id
INNER JOIN customers ON purchases.customer_id = customers.id
GROUP BY customers.id
ORDER BY "total spent";    # Ascending
``` 

```bash
SELECT customers.last_name, customers.first_name, SUM(items.price) AS "total spent" FROM items
INNER JOIN purchases ON items.id = purchases.item_id
INNER JOIN customers ON purchases.customer_id = customers.id
GROUP BY customers.id
ORDER BY "total spent" DESC;    # Descending
``` 

- CREATE TABLE:
```bash
CREATE TABLE public.users (
	id integer PRIMARY KEY,
	name character varying(100) NOT NULL
)
``` 
```bash
CREATE TABLE public.videos (
	id integer PRIMARY KEY,
	user_id integer REFERENCES public.users,  # should be a ussr which exist in users table
	name character varying(225) NOT NULL
)
```

- INSERT INTO for adding data to a table:
```bash
INSERT INTO public.users(id, name) VALUES (1, 'TOM');
``` 
```bash
INSERT INTO public.videos VALUES (1, 1, 'IN THE MOOD FOR LOVE');
``` 

-  SEQUENCE for auto-incrementing fields:
```bash
CREATE SEQUENCE user_id_seq START 4;
``` 
```bash
ALTER TABLE public.users
ALTER COLUMN id
SET DEFAULT nextval('user_id_seq');
``` 
```bash
INSERT INTO public.users(name) VALUEs ('Wayne');
``` 

- DROP TABLE for deleting tables and data:
```bash
DROP TABLE public.users RESTRICT;
``` 

```bash
DROP TABLE public.users CASCADE;
``` 

```bash
DROP TABLE IF EXISTS public.users;
``` 

-- VIEWs:
```bash
CREATE VIEW total_revenew_per_customer AS
SELECT customer.id, customers.last_name, customers.first_name, SUM(items.price) AS "total_spent" FROM items
INNER JOIN purchases ON items.id = purchases.item_id
INNER JOIN customers ON purchases.customer_id = customers.id
GROUP BY customers.id
ORDER BY "total_spent" DESC;
```
then you can call iy:
```bash
SELECT * FROM total_revenew_per_customer;
```
and also you can DROP it:
```bash
DROP VIEW total_revenew_per_customer;
```

The VIEW will be updated in the background by any change in the related TABLES.