from gen import gen
import datetime

# https://python.plainenglish.io/unit-testing-in-python-structure-57acd51da923
def test_generate_bibtex():
    gen.generate_bibtex(["Kafka: The Definitive Guide"], datetime.datetime(2017, 7, 1), ["Neha Narkhede, Gwen Shapira & Todd Palino"])