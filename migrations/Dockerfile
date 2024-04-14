FROM migrate/migrate:4 as migration

COPY migrations /migrations

ENTRYPOINT [  "migrate", "-path", "/migrations", "-database", "postgres://postgres:postgres@db:5432/weather?sslmode=disable" ]
