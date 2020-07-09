import praw
import datetime as dt
from datetime import datetime
from psaw import PushshiftAPI
import calendar
from calendar import monthrange
import json


reddit = praw.Reddit(client_id='XXXXXX',
                     client_secret='XXXXXX',
                     user_agent='XXXXXX',
                     username='XXXXXX',
                     password='XXXXXX')

abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}

api = PushshiftAPI(reddit)
