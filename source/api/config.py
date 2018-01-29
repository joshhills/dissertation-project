# App settings
app = {
    'port': 8888,
    'debug': True,
    'version': 0.2,
    'title': 'Dissertation Project API',
    'description': 'Data-mining service architecture.',
    'documentation_url': '/doc/'
}

# Messaging settings
messaging = {
    'host': 'localhost',
    'queues': {
        'work_review': 'work_review_queue',
        'work_results': 'work_results_queue',
        'work_store': 'work_store_queue',
        'global_error': 'global_error'
    }
}

# Database settings
database = {
    'host': 'couchbase://localhost',
    'username': 'root',
    'password': 'administrator'
}