import featureform as ff

postgres = ff.register_postgres(
    name="postgres-quickstart",
    host="host.docker.internal",  # The docker dns name for postgres
    port="5432",
    user="postgres",
    password="password",
    database="postgres",
)

redis = ff.register_redis(
    name="redis-quickstart",
    host="host.docker.internal",  # The docker dns name for redis
    port=6379,
)

transactions = postgres.register_table(
    name="transactions",
    variant="raw",
    table="transactions",  # This is the table's name in Postgres
)
