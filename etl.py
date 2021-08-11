import configparser
import logging

import psycopg2

from sql_queries import copy_table_queries, insert_table_queries

logging.basicConfig(level=logging.INFO)


def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read("dwh.cfg")

    logging.info("Connecting to Redshift cluster...")
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config["CLUSTER"].values()))
    cur = conn.cursor()

    logging.info("Loading staging tables...")
    # load_staging_tables(cur, conn)
    print(copy_table_queries[1])
    cur.execute(copy_table_queries[1])
    conn.commit()
    # insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
