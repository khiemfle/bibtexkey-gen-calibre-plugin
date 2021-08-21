from gen import gen
import datetime

# https://python.plainenglish.io/unit-testing-in-python-structure-57acd51da923
def test_generate_bibtex1():
    assert("narkhede2017kafka" == gen.generate_bibtex(["Neha Narkhede, Gwen Shapira & Todd Palino"], datetime.datetime(2017, 7, 1), "Kafka: The Definitive Guide"))

def test_generate_bibtex2():
    assert("kubernetes2021init-containers" == gen.generate_bibtex(["Kubernetes"], datetime.datetime(2021, 7, 1), "Init Containers"))