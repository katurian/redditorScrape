from setup import *

def scrapeComments(year, month, user):
    start_epoch=int(dt.datetime(year, abbr_to_num[month], monthrange(year, abbr_to_num[month])[0]).timestamp())
    end_epoch=int(dt.datetime(year, abbr_to_num[month], monthrange(year, abbr_to_num[month])[1]).timestamp())

    comments = list(api.search_comments(after=start_epoch, before=end_epoch,
                                author=user, limit=1000))

    data = [{'username':str(comment.author), 'body':comment.body, 'subreddit':str(comment.subreddit), 'created_at_unix':comment.created_utc, 'created_at_date':datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
                 'link':f'reddit.com/{comment.parent_id[3:]}',} for comment in comments]

    with open(f'{user}_{year}_{month}.json', 'w') as outfile:
        json.dump(data, outfile)

#scrapeComments(2016, 'Oct', 'chattypenguin')
