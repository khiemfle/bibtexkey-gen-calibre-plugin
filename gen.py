def generate_bibtex(authors, published, book_title):
    # https://github.com/kovidgoyal/calibre/blob/3dd95981398777f3c958e733209f3583e783b98c/src/calibre/db/legacy.py
    mi = db.get_metadata(book_id, index_is_id=True, get_cover=False, cover_as_data=False)

    # db.author.last_name + db.published.year + db.first two words of the book title in lower case, for example: punamusta2020were

    print(mi.authors)

    print(mi.authors[0])

    print(mi.authors[0].split(", "))

    first_author = mi.authors[0].split(", ")[0].split(" ")
    first_author_name = first_author[0]
    if len(first_author) > 1:
        first_author_name = first_author[len(first_author)-1]

    print(first_author_name)

    print(mi.pubdate)
    published_year = mi.pubdate.year

    print(published_year)

    print(mi.title)
    book_title_words = mi.title.split(" ")

    print(book_title_words)

    book_title_first_words = book_title_words[0] + book_title_words[1]

    print(book_title_first_words)

    generated_bibtex_key = (first_author_name + str(published_year) + book_title_first_words).lower()

    print(generated_bibtex_key)
    return