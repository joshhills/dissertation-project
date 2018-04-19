# Predictive Analytics for New Product Development

This project repository contains a microservice architecture and for the mass collection of Steam product data, including reviews, community updates, usage and store page listings. Its purpose was to provide data to a research project detailed in the 'wiki', however it can have other uses. Using the API, you can request that all aforementioned information for a specific product be stored. This has been used in practice on a list of product IDs tagged as 'early access'.

## Quick-Start

### Pre-requisite

A machine with [docker](https://docs.docker.com/install/) installed.

### Steps

`cd dissertation/docker`

`docker-compose up SERVICE`

The service architecture defines dependencies on the database and messaging images. Services can be deployed individually depending on your needs.

The microservices are:
- Review (data)
- Store (data)
- Update (data)
- Usage (data)
- Client (monitoring)
- Database
- Messaging

When everything is up and running:

- Couchbase Database @ port 8091
- API @ port /8888
- API Documentation @ path /doc/
- Monitoring @ port 8887

### Notes

The database image defines a volume `/mnt/dissertation`. This can be removed.
