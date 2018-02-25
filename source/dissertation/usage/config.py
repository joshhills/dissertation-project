messaging = {
    'host': '128.199.62.177',
    'queues': {
        'work_usage': 'work_usage_queue',
        'global_error': 'global_error'
    }
}

# Database settings
database = {
    'host': 'couchbase://128.199.62.177',
    'username': 'root',
    'password': 'administrator'
}

api_url = 'https://steamdb.info/api/GetGraph/?type=concurrent_max&appid={0}'
