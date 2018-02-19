FROM python:2.7

# Copy over necessary code.
COPY ./dissertation /dissertation
COPY ./docker/wait-for-it.sh /wait-for-it.sh

# Install couchbase dependencies...
RUN wget -O/etc/apt/sources.list.d/couchbase.list http://packages.couchbase.com/ubuntu/couchbase-ubuntu1404.list
RUN wget -O- http://packages.couchbase.com/ubuntu/couchbase.key | apt-key add -
RUN apt-get update
RUN apt-get install libcouchbase2-libevent libcouchbase-dev -y

# Install microservice dependencies...
RUN pip install --no-cache-dir /dissertation
RUN pip install --upgrade -r /dissertation/api/requirements.txt

# Run microservice (wait for services to become available).
CMD ["./wait-for-it.sh", "messaging:5672", "database:8093", "-t", "0", "--strict", "--", "python", "/dissertation/api/api.py"]