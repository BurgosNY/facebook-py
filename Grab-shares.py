import pandas as pd
import numpy as np
import requests
from collections import Counter
import facebook

## Use the API Key from Facebook Developer
API = ''

## Put here the downloaded csv from Facebook Insights
facebook_insights = ''

## 
graph = facebook.GraphAPI(access_token=API)

# Using a csv provided by Facebook Insights to extract the unique ids of each post in a given period.
def get_posts_ids(facebook_insights):
    
    ## using pandas to read csv:
    facedata = pd.read_csv(facebook_insights)
    ids = []
    
    ## A valid post ID is in the format (page_id_post_id). For The Marshall Project, the ID is "1442785962603494".
    ## (This is useful only for old Facebook Insights csvs. the new ones com with the right format)
    for x in range(len(facedata)):
        unique_id = facedata['Post ID']
        print unique_id
        ids.append(unique_id)
    return ids

# Function to find communities or groups that shared an individual posts. Returns list of dictionaries:
def find_shares(post_id):
    
    # Refer to Facebook Graph API here: http://facebook-sdk.readthedocs.org/en/latest/api.html
    shares = graph.get_connections(id=post_id, connection_name='sharedposts')
    
    # An empty list where we're going to put all the users/pages/communities we find:
    data2 = []
    
    # This is the basic strucure of the dictionary. We can access more things from the Facebook object. I'm keeping small.
    sharers = {'name': None, 'category': None, 'url': None}
    
    # looping throug all the available data of people that shared the post. Usually that's <5% of the total "sharers"
    # (refer to Readme file for a full explanation)
    for x in range(len(shares['data'])):
        
        # Regular FB users have only two fields (Name and id). If the length is >2, it's a page, cause or a community.
        if len(shares['data'][x]['from']) > 2:
            data = {'id': post_id, 'link': shares['data'][0]['link']}
            data['name'] = shares['data'][x]['from']['name']
            data['category'] = shares['data'][x]['from']['category']
            data['user_url'] = 'http://facebook.com/{}'.format(shares['data'][x]['from']['id'])
            data['Marshall_post'] = 'http://facebook.com/{}'.format(post_id)
            data2.append(data)
            data = {'id': None, 'link': None, 'post_link': 'http://facebook.com/{}'.format(post_id), 'name': None, 'category': None, 'user_url': None, 'Marshall_post': None}
    return data2

# A function interating through all the posts, returning a list of dictionaries.
def get_communities(facebook_insights, filename):
    posts = get_posts_ids(facebook_insights)
    data = []
    for x in posts:
        
        ## It's useful to print the ID while the function runs, so if you hit an error you'll know which post caused it. 
        print x
        data += find_shares(x)

    df = pd.DataFrame(data)
    
    # If you want to return a Pandas DaTaframe, "uncomment" the next line
    # return df
    
    # Return a csv file with the provided filename
    df.to_csv(filename, encoding='utf-8')

# Using the newly created csvfile, we can create a new one with more details:
def detail_communities(csvfile):
    facedata = pd.read_csv(csvfile)
    frequency = dict(Counter(facedata['user_url']))
    categories = ['likes', 'category', 'website', 'description', 'phone', 'link',
                  'about', 'name', 'mission']
    location = ['city', 'country', 'state']
    block = {}
    data = []
    for x in frequency.keys():
        user_id = x.split('.com/')[1]
        page = graph.get_object(id=user_id)
        block['links_shared'] = frequency[x]
        for x in categories:
            try:
                block[x] = page[x]
            except KeyError:
                block[x] = None
        for y in location:
            try:
                block[y] = page['location'][y]
            except KeyError:
                block[x] = None
        data.append(block)
        block = {}
    return data