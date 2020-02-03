class Routes(object):
    def __init__(self, app, views, rest):
        # Basic Rules
        app.add_url_rule('/', 'index', views.index)
        app.add_url_rule('/character', 'new_character', views.new_character, methods=['POST'])
        app.add_url_rule('/character/<string:charid>', 'character', views.character)
        app.add_url_rule('/characters', 'characters', views.characters)
        app.add_url_rule('/contact', 'contact', views.contact)
        app.add_url_rule('/login', 'login', views.login, methods=['GET', 'POST'])
        app.add_url_rule('/signup', 'signup', views.signup, methods=['GET', 'POST'])
        app.add_url_rule('/logout', 'logout', views.logout)
        app.add_url_rule('/licenses', 'licenses', views.licenses)

        # Rules for REST API
        app.add_url_rule('/rest/character/<string:charid>', 'rest.character', rest.character, methods=['GET', 'POST'])
