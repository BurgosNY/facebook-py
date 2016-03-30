# Facebook Community Builder

## What is this?

If you manage a page, it's always interesting to identify the biggest fans and followers. For NGOs, "causes", or politicians (among others), it is extra interesting do understand who (literally) shares your ideas and stories. This little code will get you started with Facebook Python API. It will input a Facebook Insights CSV file (which you can download through the page administrator interface) and create another csv with descriptions of the groups and pages that share your content.

## What you'll need?

* Python 2.7
* Facebook Python API (download [here](https://github.com/pythonforfacebook/facebook-sdk), documentation [here](http://facebook-sdk.readthedocs.org/en/latest/api.html))
* pandas (Python Library - [link](https://pypi.python.org/pypi/pandas/0.18.0/#downloads) or "pip install pandas")
* requests (Python Library - [link](http://docs.python-requests.org/en/master/)
* A Facebook Developer API code – [link](https://developers.facebook.com/)

## The .py file

Follow the instructions in the comments. To make it easier, put the .py and the Facebook insights csv file in the same directory. Edit the document to include your API (it only last for a couple hours) and filenames, go to terminal and type "python grab-shares.py".

* *Of course there are better ways to do all that, but the intention of this file is to make it easier for people that don't have much experience with Facebook API OR Python but need the data*.
