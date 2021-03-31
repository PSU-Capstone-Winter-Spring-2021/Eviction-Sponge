FROM evictionsponge/spongeservice:dev

ENV PORT=8080

COPY backend /src/backend
COPY frontend /src/frontend

CMD ["pipenv", "run", "uwsgi", "-b 8192", "--http-timeout", "300", "--harakiri", "300", "--enable-threads", "--master", "--processes", "2", "--http", "0.0.0.0:$PORT", "--module", "wsgi", "--die-on-term", "--uid", "nobody"]
