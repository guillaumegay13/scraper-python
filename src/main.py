from scraper import scrape_google_emails
import csv

if __name__ == "__main__":
    cities = ["Paris", "Lyon", "Marseille", "Nice", "Bordeaux"]
    search_query_base = "conciergerie location courte durée"
    num_pages = 5

    all_emails = scrape_google_emails(cities, search_query_base, num_pages)
    
    print(f"Nombre total d'emails trouvés : {len(all_emails)}")
    print("Emails trouvés :", all_emails)

    # Save emails to a CSV file
    with open('emails.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Email'])
        for email in all_emails:
            writer.writerow([email])

    print(f"Les emails ont été sauvegardés dans 'emails.csv'")