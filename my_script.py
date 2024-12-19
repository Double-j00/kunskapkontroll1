import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename="min_database.log", format='[%(asctime)s][%(levelname)s]%(message)s', level=logging.DEBUG)
logger.info("Bra")
import pandas as pd
import sqlite3
df = pd.read_csv("BE0001AJ_20241216-155513.csv")
df = df.rename(columns={"Antal b�rare efter tilltalsnamn och �r": "Antal bärare efter tilltalsnamn och år"})
df
df.info()
import pytest

def add_tree(x):
    return x + 1
def test_add_tree():
    assert add_tree(3)==4
con = sqlite3.connect("data_base.db")
df.to_sql("namn", con, if_exists="replace")