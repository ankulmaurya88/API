from .controllers import auth_controller, dashboard_controller

def register_routes(app):
    app.add_url_rule('/login', view_func=auth_controller.login, methods=['POST'])
    app.add_url_rule('/dashboard', view_func=dashboard_controller.dashboard, methods=['GET'])
