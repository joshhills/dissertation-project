"""
:author: Josh Hills

Host a bespoke service overview
to aid system inference.
"""

import config
from flask import Flask, render_template
from shared import database
from shared.model import JobState

# Global fields
app = Flask(__name__)
db = database.Couchbase(host=config.database['host'])


@app.route('/')
def index():
    """

    """
    return render_template('index.html')


@app.route('/jobs')
def jobs():
    """

    """
    results = db.run_query('SELECT * FROM job', 'job')

    job_states = []

    for row in results:
        print row
        job_states.append(JobState(row['job']))

    return render_template('jobs.html', job_states=job_states)


# Run the service
if __name__ == '__main__':
    app.run(
        host=config.app['host'],
        debug=config.app['debug'],
        port=int(config.app['port'])
    )
