from flask import g
import sqlite3


def connect_db():
    sql = sqlite3.connect('.db')
    sql.row_factory = sqlite3.Row
    return sql