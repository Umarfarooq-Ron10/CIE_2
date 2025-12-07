from library import book_details

def test_book_details():
    expected_output = (
        "Book Title: The Great Gatsby\n"
        "Author: F. Scott Fitzgerald\n"
        "Year Published: 1925\n"
        "Status: Available"
    )
    assert book_details("The Great Gatsby", "F. Scott Fitzgerald", 1925, True) == expected_output