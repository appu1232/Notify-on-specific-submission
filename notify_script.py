import time
import praw

r = praw.Reddit('Related submissions')
r.login('MSG_SENDING_ACC_USERNAME', 'PASSWORD')
print('logged onto reddit')
checked = []

blacklist = ['nsfw', 'lol']

# The topic of interest with a list of key words to match for said topic. Modify and expand as needed.
videoGames = ['legend of zelda', 'pokemon']
anime = ['steins;gate', 'steins gate', 'fma:b', 'fullmetal alchemist: brotherhood', 'fullmetal alchemist brotherhood']
politics = ['election', 'obama', 'government']
economics = ['stocks', 'wall street']

# Tuple of what will be the title of the message when a submission is found, and the specified key word list. Modify and expand as needed.
aKeyWords = [('Anime related', anime), ('Video Game related', videoGames)]
bKeyWords = [('Politics related'), worldnews, 'Economics related', economics]

while True:
    file = open('settings.txt', 'r')
    txt = file.read()
    subreddit = r.get_subreddit('askreddit')
    for submission in subreddit.get_new(limit=10):
        op_title = submission.title.lower()
        blacklist_words = any(string in op_title for string in blacklist)
        for elem in aKeyWords:
            key_words = any(string in op_title for string in elem[1])
            if ('a' in txt) and submission.id not in checked and key_words:
                if blacklist_words:
                    checked.append(submission.id)
                    break
                print('%s thread found' % elem[0].lower())
                msg = '[%s related thread](%s)' % (elem[0], submission.short_link)
                r.send_message('appu1232', '%s' % submission.title, msg)
                checked.append(submission.id)
    time.sleep(4)
    
    subreddit = r.get_subreddit('worldnews')
    for submission in subreddit.get_new(limit=10):
        op_title = submission.title.lower()
        blacklist_words = any(string in op_title for string in blacklist)
        for elem in mKeyWords:
            key_words = any(string in op_title for string in elem[1])
            if ('m' in txt) and submission.id not in checked and key_words:
                if blacklist_words:
                    checked.append(submission.id)
                    break
                print('%s thread found' % elem[0].lower())
                msg = '[%s related thread](%s)' % (elem[0], submission.short_link)
                r.send_message('MSG_RECEIVING_ACC_USERNAME', '%s' % submission.title, msg)
                checked.append(submission.id)
                break
    time.sleep(4)
    
    # Can expand down for more subreddits
