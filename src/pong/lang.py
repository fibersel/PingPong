t = gettext.translation('ru', app.conf['loc_path'], languages=['ru'])
_ = t.gettext
t.install()

_en = {
    'play': "Play",
    'play_again': "Play again",
    'you_won': "You won!",
    'you_lost': 'You lost!',
    'sign_in': 'Sign in',
    'sign_out': 'Sign out',
    'sign_up': 'Sign up',
    'leaderboars': 'Leaderboard',
    'username': 'Username',
    'password': 'Password'
    }

_rus = {k: _(_en[k]) for k in _en}

def localize(lang):
    return _en if lang == "en" else _rus