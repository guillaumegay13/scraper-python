import requests
from bs4 import BeautifulSoup
from utils import extract_emails
import time
import random

def get_google_results(query, num_pages=5):
    urls = []
    for i in range(num_pages):
        start = i * 10
        url = f"https://www.google.com/search?q={query}&start={start}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        try:
            print(f"Fetching Google results page {i+1}...")
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            for div in soup.find_all('div', class_='yuRUbf'):
                a = div.find('a')
                if a:
                    urls.append(a['href'])
            print(f"Found {len(urls)} URLs so far.")
            time.sleep(random.uniform(1, 3))  # Random delay to avoid being blocked
        except requests.RequestException as e:
            print(f"Error fetching Google results: {e}")
    return urls

def scrape_emails_from_urls(urls):
    emails_found = set()
    for i, url in enumerate(urls):
        try:
            print(f"Scraping URL {i+1}/{len(urls)}: {url}")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, timeout=10, headers=headers)
            new_emails = extract_emails(response.text)
            emails_found.update(new_emails)
            print(f"Found {len(new_emails)} new emails. Total unique emails: {len(emails_found)}")
            time.sleep(random.uniform(0.5, 1.5))  # Random delay between requests
        except requests.RequestException as e:
            print(f"Error scraping {url}: {e}")
    return list(emails_found)

def scrape_google_emails(cities, search_query_base, num_pages=5):
    all_emails = set()
    for city in cities:
        query = f"{search_query_base} {city}"
        print(f"\nSearching for: {query}")
        urls = get_google_results(query, num_pages)
        print(f"Found {len(urls)} URLs for {city}. Starting to scrape emails...")
        emails = scrape_emails_from_urls(urls)
        print(f"Emails found for {city}: {emails}")
        all_emails.update(emails)
    return list(all_emails)