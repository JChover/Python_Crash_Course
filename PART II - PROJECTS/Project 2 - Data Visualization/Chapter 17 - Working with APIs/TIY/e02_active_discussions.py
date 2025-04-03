# 17-02 Active Discussions - e02_active_discussions.py
from operator import itemgetter

import requests

from plotly.graph_objects import Bar
from plotly import offline

# Make an API Call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process the information about each submission.
submission_ids = r.json()
post_links, comments = [], []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    try:
        comments.append(response_dict['descendants'])
    except KeyError:
        print(f"No comments for submission {submission_id}")
    post_links.append(f"<a href='{f"http://news.ycombinator.com/item?id={submission_id}"}'>{response_dict['title']}</a>")

# Make visualization.
data = [{
    'type': 'bar',
    'x': post_links,
    'y': comments,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Popular Hacker News Posts',
    'xaxis': {
        'title': 'Post',
        #'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Comments',
        #'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hacker_news.html')

