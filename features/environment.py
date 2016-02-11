import ipdb
from core.services import sqlite
from identity.models.user import User


def before_scenario(context, scenario):
    sqlite.drop_all()
    sqlite.create_all()


def after_scenario(context, scenario):
    sqlite.drop_all()


def after_step(context, step):
    if step.status == "failed":
        ipdb.post_mortem(step.exc_traceback)
