## You need to change the first three values here for the code to work properly.


## Use the API Key from Facebook Developer
API = ''

## Put here your page id (default is The Marshall Project's ID)
page_id = ''

## Put here the names of the output files
report = 'example.csv'
detailed_report = 'example_detail.csv'

## Importing the libraries
import pandas as pd
import requests
import facebook

graph = facebook.GraphAPI(access_token=API)

# Using a csv provided by Facebook Insights to extract the unique ids of each post in a given period.

# To test the function, you can run this part, which retrieves only the shares of the last 30 posts.
def get_posts_ids_sample(page_id):
    posts = graph.get_connections(id=page_id, connection_name='posts')
    allposts = []
    for post in posts['data']:
        allposts.append(post['id'])
    return allposts

def get_posts_ids(page_id):
    posts = graph.get_connections(id=page_id, connection_name='posts')
    allposts = []
    while(True):
        try:
            for post in posts['data']:
                allposts.append(post['id'])
            # Attempt to make a request to the next page of data, if it exists.
            posts=requests.get(posts['paging']['next']).json()
        except KeyError:
            # When there are no more pages (['paging']['next']), break from the
            # loop and end the script.
            break
    return allposts


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
def get_communities(page_id, report):
    posts = get_posts_ids(page_id)
    data = []
    for x in posts:
        try:
            data += find_shares(x)
        except TypeError:
            continue


    df = pd.DataFrame(data)
    print 'Found ' + str(len(df)) + ' shares by pages'
    
    # If you want to return a Pandas DaTaframe, "uncomment" the next line
    # return df
    
    # Return a csv file with the provided filename
    df.to_csv(report, encoding='utf-8')

# Using the newly created csvfile, we can create a new one with more details:
def detail_communities(report, detailed_report):
    from collections import Counter 
    facedata = pd.read_csv(report)
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
    df = pd.DataFrame(data)
    print 'Found the details of ' + str(len(df)) + ' pages'
    print 'open ' + report + ' and ' + detailed_report + ' in this folder for more information'
    print '\n'
    df.to_csv(detailed_report, encoding='utf-8')



## Running the functions
get_communities(page_id, report)
detail_communities(report, detailed_report)
