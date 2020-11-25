def print_book_info(title, author=None, year=None):
    output = f'"{title}"'
    if author or year:
        output += " was written"
        if author:
            output += f" by {author}"
        if year:
            output += f" in {year}"
    print(output)
