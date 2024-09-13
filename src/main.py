from scraper import scrape_google_emails
import csv

if __name__ == "__main__":
    cities = ["Paris", "Lyon", "Marseille", "Nice", "Bordeaux"]
    search_query_base = "conciergerie location courte durée"
    num_pages = 2  # Reduced for faster testing

    all_emails = scrape_google_emails(cities, search_query_base, num_pages)
    
    print(f"\nTotal number of unique emails found: {len(all_emails)}")
    print("Emails found:", all_emails)

    # Save emails to a CSV file
    with open('emails.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Email'])
        for email in all_emails:
            writer.writerow([email])

    print(f"Emails have been saved to 'emails.csv'")