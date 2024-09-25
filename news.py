import requests
from bs4 import BeautifulSoup

# Function to fetch news from Google
def get_google_news(search_term, num_articles=5):
    # Google News search URL
    search_url = f"https://www.google.com/search?q={search_term}&tbm=nws"
    
    # Set User-Agent to mimic a browser request to avoid blocking
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    
    # Make the request to Google
    response = requests.get(search_url, headers=headers)
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Debug: Print the response status and HTML structure to check if the page was fetched correctly
    print("Response status code:", response.status_code)
    print("Page title:", soup.title.string)  # Ensure we are on the correct page

    # Find all the news article elements
    articles = soup.find_all('div', class_='BVG0Nb')  # Updated class to match current Google News structure

    # If no articles are found, print a message and return
    if not articles:
        print(f"No articles found for search term: {search_term}")
        return []

    # Store the extracted articles
    news_articles = []

    for idx, article in enumerate(articles[:num_articles]):
        # Extracting the title and URL
        title = article.find('div', class_='mCBkyc').get_text()
        link = article.a['href']
        source = article.find('div', class_='BNeawe UPmit AP7Wnd').get_text()

        news_articles.append({
            'title': title,
            'url': f"https://www.google.com{link}",
            'source': source
        })

    return news_articles

# Function to display the news
def display_news(news_articles, title="News"):
    print(f"\n==== {title} ====")
    if not news_articles:
        print("No articles found.")
    for idx, article in enumerate(news_articles, 1):
        print(f"{idx}. {article['title']}")
        print(f"   Source: {article['source']}")
        print(f"   URL: {article['url']}\n")

# Main function
def main():
    # Fetch Indian news
    search_term_india = "India news"
    indian_news = get_google_news(search_term_india)
    display_news(indian_news, "Indian News")

    # Fetch International news
    search_term_international = "International news"
    international_news = get_google_news(search_term_international)
    display_news(international_news, "International News")

if __name__ == '__main__':
    main()
