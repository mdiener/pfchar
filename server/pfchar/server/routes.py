class Routes(object):
    def __init__(self, app, views, rest):
        app.add_url_rule('/', 'index', views.index)
        app.add_url_rule('/character', 'character', views.character)
        app.add_url_rule('/characters', 'characters', views.characters)
        app.add_url_rule('/contact', 'contact', views.contact)
        app.add_url_rule('/login', 'login', views.login, methods=['GET', 'POST'])
        app.add_url_rule('/signup', 'signup', views.signup, methods=['GET', 'POST'])
        app.add_url_rule('/logout', 'logout', views.logout)
