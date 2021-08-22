from gen import gen
import datetime

# https://python.plainenglish.io/unit-testing-in-python-structure-57acd51da923
def test_generate_bibtex1():
    cases = [
        ["narkhede2017kafka-ktdg", ["Neha Narkhede, Gwen Shapira & Todd Palino"], datetime.datetime(2017, 7, 1), "Kafka: The Definitive Guide"],
        ["kubernetes2021init-containers", ["Kubernetes"], datetime.datetime(2021, 7, 1), "Init Containers"],
        ["aws2020aws-acliug", ["AWS"], datetime.datetime(2020, 7, 1), "AWS Command Line Interface - User Guide"],
        ["author2019were-wrc",["An author"], datetime.datetime(2019, 7, 1), "We're really cool"],
        ["author2019weetxt",["An author"], datetime.datetime(2019, 7, 1), "wee.txt"],
        ["author2019were-wrc",["An author"], datetime.datetime(2019, 7, 1), "We`re really cool"],
        ["author2019were-wrc",["An author"], datetime.datetime(2019, 7, 1), "We´re really cool"],
        ["katz2019introduction-itmcpapchcanss",["Jonathan Katz & Yehuda Lindell"], datetime.datetime(2019, 7, 1), "Introduction to Modern Cryptography: Principles and Protocols (Chapman & Hall/CRC Cryptography and Network Security Series)"]
    ]

    for case in cases:
        assert(case[0] == gen.generate_bibtex(case[1], case[2], case[3]))