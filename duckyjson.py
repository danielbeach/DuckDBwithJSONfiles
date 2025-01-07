import duckdb
import os

KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
SECRET = os.environ['AWS_SECRET_ACCESS_KEY']

conn = duckdb.connect()

conn.query("""
               INSTALL httpfs;
               LOAD httpfs;
                CREATE SECRET secretaws (
                TYPE S3,
                PROVIDER CREDENTIAL_CHAIN
            );
               """)

df = conn.query("""
                SELECT *
                FROM read_json('s3://confessions-of-a-data-guy/JSON/crappycrap.json')
                LIMIT 5;
                """)
df.show()

# doing some aggregations
# not you can read multiple files with a wild card
df = conn.query("""
                SELECT CAST(timestamp AS DATE) AS date, SUM("Sales Count") as sales_count
                FROM read_json('s3://confessions-of-a-data-guy/JSON/crappycrap*.json')
                GROUP BY CAST(timestamp AS DATE)
                ORDER BY date;
                """)
df.show()
