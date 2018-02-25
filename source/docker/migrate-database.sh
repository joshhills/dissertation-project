#!/bin/sh

set -x
set -m

/entrypoint.sh couchbase-server &

if [ ! -d "/opt/couchbase/var/lib/couchbase/data" ]; then
    /opt/couchbase/wait-for-it.sh localhost:8091 -t 0 --strict

    echo "Setting up database..."

    # Set up index RAM quota.
    curl -X POST http://127.0.0.1:8091/pools/default \
    -d memoryQuota=1000 -d indexMemoryQuota=300
    echo "Index RAM quota completed"

    # Setup services
    curl http://localhost:8091/node/controller/setupServices \
    -d services=kv%2Cn1ql%2Cindex
    echo "Services completed"

    # Set up credentials
    curl -X POST http://localhost:8091/settings/web \
    -d 'password=administrator&username=root&port=SAME'
    echo "Credentials completed"

    # Set up buckets
    curl -u root:administrator -X POST \
    http://localhost:8091/pools/default/buckets \
    -d 'flushEnabled=1&threadsNumber=3&replicaIndex=0&replicaNumber=0&ramQuotaMB=100&bucketType=membase&name=job&authType=sasl&saslPassword='

    curl -u root:administrator -X POST \
    http://localhost:8091/pools/default/buckets \
    -d 'flushEnabled=1&threadsNumber=3&replicaIndex=0&replicaNumber=0&ramQuotaMB=300&bucketType=membase&name=review&authType=sasl&saslPassword='

    curl -u root:administrator -X POST \
    http://localhost:8091/pools/default/buckets \
    -d 'flushEnabled=1&threadsNumber=3&replicaIndex=0&replicaNumber=0&ramQuotaMB=200&bucketType=membase&name=update&authType=sasl&saslPassword='

    curl -u root:administrator -X POST \
    http://localhost:8091/pools/default/buckets \
    -d 'flushEnabled=1&threadsNumber=3&replicaIndex=0&replicaNumber=0&ramQuotaMB=100&bucketType=membase&name=store&authType=sasl&saslPassword='

    curl -u root:administrator -X POST \
    http://localhost:8091/pools/default/buckets \
    -d 'flushEnabled=1&threadsNumber=3&replicaIndex=0&replicaNumber=0&ramQuotaMB=250&bucketType=membase&name=usage&authType=sasl&saslPassword='

    # Set up indexes
    curl -u root:administrator -X POST \
    http://localhost:8091/settings/indexes \
    -d 'indexerThreads=0&logLevel=info&maxRollbackPoints=5&memorySnapshotInterval=200&stableSnapshotInterval=5000&storageMode=forestdb'

    /opt/couchbase/wait-for-it.sh  localhost:8093 -t 0 --strict

    sleep 10

    curl -u root:administrator \
    http://localhost:8093/query/service \
    -d 'statement=CREATE PRIMARY INDEX ON `job`'

    curl -u root:administrator \
    http://localhost:8093/query/service \
    -d 'statement=CREATE PRIMARY INDEX ON `review`'

    curl -u root:administrator \
    http://localhost:8093/query/service \
    -d 'statement=CREATE PRIMARY INDEX ON `update`'

    curl -u root:administrator \
    http://localhost:8093/query/service \
    -d 'statement=CREATE PRIMARY INDEX ON `store`'

    curl -u root:administrator \
    http://localhost:8093/query/service \
    -d 'statement=CREATE PRIMARY INDEX ON `usage`'

    echo "Buckets completed"
fi

fg