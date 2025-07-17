from src.forms.todos_form import TodosForm
from src.repos.sessions_repos import SessionsRepos
from src.repos.todos_repos import TodosRepos
from src.repos.users_repos import UsersRepos
from flask import request
import json

class TodosRoutes:
    def __init__(self, app):

        @app.route('/todos')
        def todos():
            user = self.current_user()
            if not user:
                return self.unauthorized()

            return TodosRepos.get(user)

        @app.route('/todos', methods=['POST'])
        def create_todos():
            user = self.current_user()
            if not user:
                return self.unauthorized()

            form = TodosForm.from_json(request.get_json())
            if not form.validate():
                return json.dumps(form.errors), 422

            todo = TodosRepos.create_todo(user, {
               "item": form.item.data,
                "category": form.category.data
            })
            return {'message': 'Data Received','data': todo}, 200

    def unauthorized(self):
        return json.dumps({'error': 'You must be logged in.'}), 401

    def current_user(self):
        authorization = request.headers.get('authorization')
        if not authorization:
            return None

        session = SessionsRepos.get(authorization)

        return UsersRepos.get(session['user_id'])

