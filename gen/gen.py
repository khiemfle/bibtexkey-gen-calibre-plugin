from functools import reduce

articles = ["a", "an", "the"]

special_chars = [":", "'", "`", "´", "-", "_", "&", "."]

def generate_bibtex(authors, published, book_title):
    print(authors)

    nomalized_authors = authors[0].replace("&,", ",").replace(", ", ",").replace("&", ",").replace(";", ",")

    first_author = nomalized_authors.split(",")[0].split(" ")
    first_author_last_name = first_author[0]
    if len(first_author) > 1:
        first_author_last_name = first_author[len(first_author)-1]

    print(first_author_last_name)

    print(published)
    published_year = published.year

    print(published_year)

    print(book_title)
    book_title_words = book_title.split(" ")

    for sc in special_chars:
        book_title_words = list(map(lambda x: x.replace(sc, ""), book_title_words))

    print(map(lambda x: x[0], book_title_words))
    first_letter_group = "".join(list(map(lambda x: x[0] if len(x) > 0 else "", book_title_words)))

    book_title_words = list(filter(lambda x: x.lower() not in articles, book_title_words))

    print(book_title_words)

    if len(book_title_words) == 2:
        book_title_first_words = book_title_words[0] + "-" + book_title_words[1]
    elif len(book_title_words) == 1:
        book_title_first_words = book_title_words[0]
    else:
        book_title_first_words = book_title_words[0] + "-" + first_letter_group

    print(book_title_first_words)

    generated_bibtex_key = (first_author_last_name + str(published_year) + book_title_first_words).lower()

    print(generated_bibtex_key)
    return generated_bibtex_key