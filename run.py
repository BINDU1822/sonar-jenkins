def scrape_website():
    # Make a request to the website
    r = requests.get("https://books.toscrape.com")
 
    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(r.text, 'html.parser')
 
    # Find all the books on the page
    books = soup.find_all('article', class_='product_pod')
 
    # Initialize empty list for storing book details
    book_details = []
 
    # Iterate through each book and get details
    for book in books:
        title = book.h3.a.get('title')
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        book_details.append([title, price, availability])
 
    # Write the book details to a CSV file
    with open('/tmp/book_details.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Price', 'Availability'])
        writer.writerows(book_details)
