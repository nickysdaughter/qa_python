# qa_python

 This repository contains a suite of unit tests designed for a BookCollector class that manages a collection of books, their genres, and favorite books. The tests utilize the pytest framework to ensure the functionality of various features.

## Features Tested

Adding New Books

Confirm that a new book can be added to the collection.
Validate that adding a book with an empty name or a name exceeding 40 characters is handled correctly.
Setting Book Genres

Check the ability to assign a genre to a newly added book.
Test the behavior when trying to set a genre for a non-existent genre.
Retrieving Book Genres

Verify that the correct genre is returned for an existing book.
Ensure that the method to get books by a specific genre works as expected.
Handling Children’s Books

Test if the correct number of children’s books can be retrieved based on their genres.
Managing Favorite Books

Confirm that books can be added to and removed from favorites.
Check behavior when attempting to delete a non-existent favorite book.
Testing Framework

These tests are built using the pytest framework. To run the tests, ensure you have pytest installed in your Python environment. You can install it using pip:
 
```pip install pytest```
## Running the Tests

To execute the tests, navigate to the directory containing the test file and run the following command in your terminal:

 
```pytest -v tests.py```
The -v option provides verbose output, displaying each test as it runs.

## Test Cases Overview

Here’s a brief description of the test cases included in the suite:

- test_add_new_book_one_book: Tests the addition of a single book.
- test_add_new_book_more_40_or_zero_name_chars: Tests adding books with invalid names (empty or too long).
- test_set_book_genre_new_genre: Tests setting a genre for a new book.
- test_set_book_genre_non_existent_genre: Tests setting a genre for a book with a non-existent genre.
- test_get_book_genre_existing_genre: Tests retrieving a genre for an existing book.
- test_get_books_with_specific_genre: Tests retrieving books by a specific genre.
- test_get_books_genre_two_books: Tests retrieving all books in the collection.
- test_get_books_for_children_one_book: Tests retrieving children's books.
- test_add_book_in_favorites_new_book: Tests adding a book to favorites.
- test_add_book_in_favorites_already_added_book: Tests adding an already favorited book.
- test_delete_book_from_favorites_empty_list: Tests deleting a book from favorites when the list is empty.
- test_get_list_of_favorites_books_one_book: Tests retrieving the list of favorite books.
