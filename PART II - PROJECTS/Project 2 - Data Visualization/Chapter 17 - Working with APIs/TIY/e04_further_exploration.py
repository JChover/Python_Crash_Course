# 17-04 Further Exploration - e04_further_exploration.py
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
posts = []  # List to store tuples of (post_link, comment_count)
for submission_id in submission_ids[:15]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    # Retrieve the number of comments; default to 0 if missing.
    post_type = response_dict.get('type', 0)
    # Retrieve the score; default to 0 if missing.
    score_count = response_dict.get('score', 0)
    # Build the post link.
    post_link = f"<a href='http://news.ycombinator.com/item?id={submission_id}'>{response_dict['title']}</a>"
    posts.append((post_link, post_type, score_count))

# Sort posts by comment count in descending order.
sorted_posts = sorted(posts, key=lambda post: post[2], reverse=True)
# Unzip the sorted posts into separate lists.
post_links, types, scores = zip(*sorted_posts)

# Make visualization.
data = [{
    'type': 'bar',
    'x': post_links,
    'y': scores,
    'hovertext': types,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Popular Hacker News Posts, sorted by number by Score',
    'xaxis': {
        'title': 'Post',
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Score',
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hacker_news.html')
