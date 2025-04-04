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
posts = []  # List to store tuples of (post_link, comment_count)
for submission_id in submission_ids[:15]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    # Retrieve the number of comments; default to 0 if missing.
    comment_count = response_dict.get('descendants', 0)
    # Build the post link.
    post_link = f"<a href='http://news.ycombinator.com/item?id={submission_id}'>{response_dict['title']}</a>"
    posts.append((post_link, comment_count))

# Sort posts by comment count in descending order.
sorted_posts = sorted(posts, key=lambda post: post[1], reverse=True)
# Unzip the sorted posts into separate lists.
post_links, comments = zip(*sorted_posts)

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
    'title': 'Popular Hacker News Posts, sorted by number of Comments',
    'xaxis': {
        'title': 'Post',
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Comments',
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hacker_news.html')
