import time
import praw

r = praw.Reddit('Related submissions')
r.login('appubot', 'appu2844')
print('logged onto reddit')
checked = []

blacklist = ['recommend', 'recommendation', 'recomend', 'recommendations', 'suggest', 'suggestion', 'sugest', 'suggestions']

steinsGateWords = ["steins;gate", "stiens;gate", "s;g", "steins", "stiens", "steins gate", "stiens gate", "steinsgate", "stiensgate", "stein's gate", "stien's gate", "stein's;gate", "stien's;gate", "stein'sgate", "stien'sgate", "steyns;gate", "stayns;gate", "steyns gate", "stayns gate", "steynsgate", "staynsgate", "okabe", "kurisu", "makise", 'mayuri', "steins;gate0", "stiens;gate0", "steinsgate0", "stiensgate0"]
madokaWords = ['madoka', 'madoko', 'modoka', 'modoko', 'madaka', 'homura']
tomoChanWords = ['tomo chan', 'tomo-chan']
lastGameWords = ['last game', 'last gaem']
horimiyaWords = ['horimiya', 'horymiya', 'horimia']
kawaiijoWords = ['kawaii joushi o komarasetai', 'kawaii joushi wo komarasetai', 'kawai joushi o komarasetai', 'kawai joushi wo komarasetai']
bokuDakeWords = ['boku dake', 'bokudake', 'bokumachi']
RELIFEWords = ['relife', 'rilife']
shokugekiWords = ['shokugeki no souma', 'shokugeki no soma', 'shokugiki no souma', 'shokugiki no soma']
animeKeyWords = [('Steins;Gate', steinsGateWords), ('Madoka Magica', madokaWords), ('Last Game', lastGameWords), ('ReLIFE', RELIFEWords)]
mangaKeyWords = [('Tomo', tomoChanWords), ('Last Game', lastGameWords), ('Horimiya', horimiyaWords), ('KawaiiJo', kawaiijoWords), ('ReLIFE', RELIFEWords), ('Shokugeki', shokugekiWords)]

while True:
    file = open('C:/Users/Deepak/Desktop/settings.txt', 'r')
    file = file.read()
    subreddit = r.get_subreddit('anime')
    for submission in subreddit.get_new(limit=10):
        op_title = submission.title.lower()
        blacklist_words = any(string in op_title for string in blacklist)
        for anime in animeKeyWords:
            key_words = any(string in op_title for string in anime[1])
            if ('a' in file) and submission.id not in checked and key_words:
                if blacklist_words:
                    checked.append(submission.id)
                    break
                print('%s thread found' % anime[0].lower())
                msg = '[%s related thread](%s)' % (anime[0], submission.short_link)
                r.send_message('appu1232', '%s' % submission.title, msg)
                checked.append(submission.id)
        if ('q' in file) and submission.id not in checked and (submission.title.lower().startswith(('what', 'which', 'who', 'when')) and submission.title.lower().endswith('?')):
            print('question thread found')
            if blacklist_words:
                checked.append(submission.id)
            else:
                msg = '[%s](%s)' % (submission.title, submission.short_link)
                r.send_message('appu1232', '%s' % submission.title, msg)
                checked.append(submission.id)
    time.sleep(4)
    
    subreddit = r.get_subreddit('manga')
    for submission in subreddit.get_new(limit=10):
        op_title = submission.title.lower()
        blacklist_words = any(string in op_title for string in blacklist)
        for manga in mangaKeyWords:
            key_words = any(string in op_title for string in manga[1])
            if ('m' in file) and submission.id not in checked and key_words:
                if blacklist_words:
                    checked.append(submission.id)
                    break
                print('%s thread found' % manga[0].lower())
                msg = '[%s related thread](%s)' % (manga[0], submission.short_link)
                r.send_message('appu1232', '%s' % submission.title, msg)
                checked.append(submission.id)
                break
    time.sleep(4)