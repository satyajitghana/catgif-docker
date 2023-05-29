from flask import Flask, render_template
import redis

app = Flask(__name__)

# set up a connection to Redis
r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def index():
    # increment the visitor count
    r.incr('visits')
    visits = r.get('visits').decode('utf-8')
    
    return render_template('index.html', url="https://cataas.com/cat/gif", visits=visits)
