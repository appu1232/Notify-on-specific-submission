import time
import praw

# Enter your main account's username here (the one that will recieve the notifications).
main_acc = 'USERNAME'

# Enter your second Reddit account username and password here. Make sure this second account has at least 3 link karma or it will not work.
second_acc = 'USERNAME'
second_acc_pass = 'PASSWORD'

r = praw.Reddit('Related submissions')
r.login(second_acc, second_acc_pass)
print('logged onto reddit')
checked = []

# Blacklisted words. If a post has any of these words, it will not detect it as a match and a notification will not be sent.
blacklist = ['nsfw', 'nsfl', 'lol']

# The topic of interest with a list of key words to match for said topic. Modify and expand as needed.
videoGames = ['legend of zelda', 'pokemon']
anime = ['steins;gate', 'steins gate', 'fma:b', 'fullmetal alchemist: brotherhood', 'fullmetal alchemist brotherhood']
politics = ['election', 'obama', 'government']
economics = ['stocks', 'wall street']
# Add more if you want

# Tuple of what will be the title of the message when a submission is found, and the specified key word list. Modify and expand as needed.
# There are multiple lists of tuples here to show that you can use more than one set of words to match. For example, if you want to search for both politics and economics in one subreddit, you would use the bkeyWords list.
aKeyWords = [('Anime related', anime), ('Video Game related', videoGames)]
bKeyWords = [('Politics related'), worldnews, ('Economics related', economics)]
# Add more if you want

# Main loop.
while True:
    # Open settings file. Settings file is used to determine which subreddits to check. Modify settings file if you want to check one subreddit but the other. More details in README.
    file = open('settings.txt', 'r')
    txt = file.read()
    file.close()
    # AskReddit search.
    subreddit = r.get_subreddit('askreddit')
    # Loops through latest 10 submission on AskReddit.
    for submission in subreddit.get_new(limit=5):
        # Title of post
        post_title = submission.title.lower()
        blacklist_words = any(string in post_title for string in blacklist)
        if blacklist_words:
            checked.append(submission.id)
        # Loop through tuple (and in turn, the key words of said tuple) for key word matches in the title of the post.
        for elem in aKeyWords:
            key_words = any(string in post_title for string in elem[1])
            # If the sub AskReddit is enabled, send message when key word submission is found.
            if ('askreddit' in txt) and submission.id not in checked and key_words:
                # Not a match if matched with a blacklisted word.
                # Optional, delete if you want.
                print('%s thread found' % elem[0].lower())
                # Message title with link to submission.
                msg = '[%s related thread](%s)' % (elem[0], submission.short_link)
                r.send_message(main_acc, '%s' % submission.title, msg)
                checked.append(submission.id)
                break
    # Reddit API encourages that subsequent calls to servers have at least a 2 second delay. Feel free to increase the sleep time but please stay above 2.
    time.sleep(4)
    
    # Same deal. Search for keywords (bkeyWords) in the worldnews subreddit.
    subreddit = r.get_subreddit('worldnews')
    for submission in subreddit.get_new(limit=5):
        post_title = submission.title.lower()
        blacklist_words = any(string in post_title for string in blacklist)
        if blacklist_words:
            checked.append(submission.id)
        for elem in mKeyWords:
            key_words = any(string in post_title for string in elem[1])
            if ('worldnews' in txt) and submission.id not in checked and key_words:
                print('%s thread found' % elem[0].lower())
                msg = '[%s related thread](%s)' % (elem[0], submission.short_link)
                r.send_message(main_acc', '%s' % submission.title, msg)
                checked.append(submission.id)
                break
    # Stay above 2.
    time.sleep(4)
    
    # Can expand down for more subreddits. Copy paste the cluster from 'subreddit = ...' down to time.sleep and change subreddit name and keyword tuple as needed.
    # Also make sure to add the new subreddit to the settings.txt file
