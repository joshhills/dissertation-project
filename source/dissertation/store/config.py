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

api_url_1 = 'http://store.steampowered.com/api/appdetails?appids={0}'
api_url_2 = 'https://steamspy.com/api.php?request=appdetails&appid={0}'
