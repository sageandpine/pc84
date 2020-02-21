# pinecones copy of magic 8 ball for python 9 positive 6 uncertain 5 negative
import random
answers = ['It is certain,YO!', 'Totes decided in the affirmative',
'Without a doubt home skillet', 'Put a fork in it-it is DONE!',
'Pop the champagne!', 'Lookin good!!!!', 'Bet!', 'Most def!',
'YEEEEAAAAAHHHH! OKAY!',
'Going to have to ask again later, the future is hazy.',
'Better if I tell you another time', 'I got nothin.',
'Sometimes, its best not to say. This is sometime.',
'Cannot predict now', 'Concentrate harder and ask again',
'Nope. Definitely not!', 'I wish it were so, but it looks as though-NOPE',
'Awwwww. Sucks for you!', 'That is a negative',
'No, just remember that disaapointment represents reality snapped into focus.']
print('  __  __          ____  _____ _____    ___  ')
print(' |  \/  |   /\   / ____|_    / ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ___\ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/     \_\____|_____\_____|  \___/  by******')
print('               ____     ____   ___      __ ')
print('        ***** |  _ \  /_____| / _ \   / _  |')
print('              | | | || |     | (_) | / /_| |_')
print('              |  _ / | |      > _ <  \ __   _|')
print('              | |    | |____ | (_) |     | |')
print('              |_|     \_____| \___/      |_|*****')
print('**imaginary_friend_programs**')
print('What is Up?! I am the Magic 8 ball, What is your name?')
name = input()
print('Hey ' + name)


def Magic8Ball():
    print('Ask me a question.')
    input()
    print (answers[random.randint(0, len(answers)-1)] )
    print('I hope that helped!')
    Replay()


def Replay():
    print ('Do you have another question? [Y/N] ')
    reply = input()
    if reply == 'Y':
        Magic8Ball()
    elif reply == 'N':
        exit()
    else:
        print('I apologise, I did not catch that. Please repeat.')
        Replay()


Magic8Ball()
