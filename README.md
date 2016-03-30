# Facebook Community Builder

## What is this?

If you manage a page, it's always important to identify the biggest fans and followers. For NGOs, "causes", or politicians (among others), it is extra interesting do understand who (literally) shares your ideas and stories. This little code will get you started with Facebook Python API. It will take a Facebook Insights CSV file as an input (which you can download through the page administrator interface) and create two other csvs with descriptions of the communities, pages and public figures that share your content[^1].

## What you'll need?

* Python 2.7
* Facebook Python API (download [here](https://github.com/pythonforfacebook/facebook-sdk), documentation [here](http://facebook-sdk.readthedocs.org/en/latest/api.html))
* pandas (Python Library - [link](https://pypi.python.org/pypi/pandas/0.18.0/#downloads) or "pip install pandas")
* requests (Python Library - [link](http://docs.python-requests.org/en/master/)
* A Facebook Developer API code – [link](https://developers.facebook.com/)

## The .py file

Follow the instructions in the comments. To make it easier, put the .py and the Facebook insights csv file in the same directory. Edit the document to include your API (it only last for a couple hours) and filenames, go to terminal and type "python grab-shares.py".

* *Of course there are better ways to do all that, but the intention of this file is to make it easier for people that don't have much experience with Facebook API OR Python but need the data*. 

[^1] Right now, Facebook will only show a fraction of the people that shared the page through the API. This is [by design](https://developers.facebook.com/bugs/1404733043148335/), and the limitations are related to privacy settings of the pages that shared the info.
