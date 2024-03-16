import requests

def lookup_book_by_isbn(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if f"ISBN:{isbn}" in data:
            return data[f"ISBN:{isbn}"]
    return None

if __name__ == "__main__":
    isbn = input("Enter the ISBN of the book: ")
    book_details = lookup_book_by_isbn(isbn)
    if book_details:
        print("Book Details:")
        print("Title:", book_details.get('title', 'N/A'))
        print("Authors:", ', '.join(author.get('name', 'N/A') for author in book_details.get('authors', [])))
        print("Publish Date:", book_details.get('publish_date', 'N/A'))
    else:
        print("Book not found.")
