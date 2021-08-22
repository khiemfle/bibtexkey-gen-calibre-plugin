from gen import gen
import datetime

# https://python.plainenglish.io/unit-testing-in-python-structure-57acd51da923
def test_generate_bibtex1():
    assert("narkhede2017kafka-ktdg" == gen.generate_bibtex(["Neha Narkhede, Gwen Shapira & Todd Palino"], datetime.datetime(2017, 7, 1), "Kafka: The Definitive Guide"))

def test_generate_bibtex2():
    assert("kubernetes2021init-containers" == gen.generate_bibtex(["Kubernetes"], datetime.datetime(2021, 7, 1), "Init Containers"))

def test_generate_bibtex3():
    assert("aws2020aws-acliug" == gen.generate_bibtex(["AWS"], datetime.datetime(2020, 7, 1), "AWS Command Line Interface - User Guide"))

def test_generate_bibtex4():
    assert("author2019were-wrc" == gen.generate_bibtex(["An author"], datetime.datetime(2019, 7, 1), "We're really cool"))

def test_generate_bibtex5():
    assert("author2019weetxt" == gen.generate_bibtex(["An author"], datetime.datetime(2019, 7, 1), "wee.txt"))
    
def test_generate_bibtex6():
    assert("author2019were-wrc" == gen.generate_bibtex(["An author"], datetime.datetime(2019, 7, 1), "We`re really cool"))

def test_generate_bibtex7():
    assert("author2019were-wrc" == gen.generate_bibtex(["An author"], datetime.datetime(2019, 7, 1), "We´re really cool"))

def test_generate_bibtex8():
    assert("katz2019introduction-itmcpapchcanss" == gen.generate_bibtex(["Jonathan Katz & Yehuda Lindell"], datetime.datetime(2019, 7, 1), "Introduction to Modern Cryptography: Principles and Protocols (Chapman & Hall/CRC Cryptography and Network Security Series)"))
