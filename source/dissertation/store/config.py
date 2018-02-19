messaging = {
    'host': 'localhost',
    'queues': {
        'work_store': 'work_store_queue',
        'global_error': 'global_error'
    }
}

# Database settings
database = {
    'host': 'couchbase://database',
    'username': 'root',
    'password': 'administrator'
}

api_url = 'http://store.steampowered.com/api/appdetails?appids={0}'
