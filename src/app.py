from typing import NewType
from flask import Flask
from flask_injector import FlaskInjector, request
from injector import Scope, inject
from abc import abstractmethod, ABC

ConnectionString = NewType("ConnectionString", str)


class AbstractDatabase(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def connect(self) -> str:
        pass


class MySqlDatabase(AbstractDatabase):
    @inject
    def __init__(self, connection_string: ConnectionString):
        super().__init__()
        self.connection_string = connection_string

    def connect(self):
        return "MySqlDatabase " + self.connection_string


class PostgreSqlDatabase(AbstractDatabase):
    @inject
    def __init__(self, connection_string: ConnectionString):
        super().__init__()
        self.connection_string = connection_string

    def connect(self):
        return "PostgreDatabase " + self.connection_string


class MyService:
    @inject
    def __init__(self, db: AbstractDatabase):
        self.db = db

    def get_data(self):
        return self.db.connect()


def configure(binder):
    binder.bind(ConnectionString, to="a", scope=request)
    binder.bind(MyService, to=MyService, scope=request)
    binder.bind(AbstractDatabase, to=MySqlDatabase, scope=request)


app = Flask(__name__)


@inject
@app.route("/data")
def my_flask_route(service: MyService):
    return service.get_data()


FlaskInjector(app=app, modules=[configure])
