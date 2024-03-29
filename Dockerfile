version: "3"
services:
web:
build: ./app
ports:
- 5000:5000
depends_on:
- mongo
mongo:
image: mongo:latest
volumes:
- mongo-data:/data/db
volumes:
mongo-data: