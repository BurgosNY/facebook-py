# Facebook Community Builder

## What is this?

If you manage a page, it's always important to identify the biggest fans and followers. For NGOs, "causes", or politicians (among others), it is extra interesting do understand who (literally) shares your ideas and stories. This little code will get you started with Facebook Python SDK. To make it easier to visualize what the script is doing, it will take a Facebook Insights CSV file as an input (which you can download through the page administrator interface) and create two other csvs with descriptions of the communities, pages and public figures that share your content[^1].

## What you'll need?

* Python 2.7
* Facebook Python SDK (download [here](https://github.com/pythonforfacebook/facebook-sdk), documentation [here](http://facebook-sdk.readthedocs.org/en/latest/api.html))
* pandas (Python Library - [link](https://pypi.python.org/pypi/pandas/0.18.0/#downloads) or "pip install pandas")
* requests (Python Library - [link](http://docs.python-requests.org/en/master/ or "pip install requests")
* A Facebook Developer Acces Token code – [link](https://developers.facebook.com/)

## The .py file

Follow the instructions in the comments. To make it easier to manipulate, put the .py and the Facebook insights csv file in the same directory. Edit the document to include your API (it only lasts for a couple of hours), Facebook Insihts filename and desired output filenames. Now grab and drop the folder in the terminal and type "python grab-shares.py".

## Additional info

There are better ways to do all that is described here, in fancier interfaces, but the intention of this file is to make it easier for people who don't have much experience with Facebook API OR Python but need the data to get started.


[^1] Right now, Facebook will only show a fraction of the people that shared the page through the API. This is [by design](https://developers.facebook.com/bugs/1404733043148335/), and the limitations are related to privacy settings of the pages that shared the info.
