def book_details(title, author, year, available):
    status = "Available" if available else "Not Available"
    result = (
        f"Book Title: {title}\n"
        f"Author: {author}\n"
        f"Year Published: {year}\n"
        f"Status: {status}"
    )
    return result

if __name__ == "__main__":
    title = "The Great Gatsby"
    author = "F. Scott Fitzgerald"
    year = 1925
    available = True

    print(book_details(title, author, year, available))