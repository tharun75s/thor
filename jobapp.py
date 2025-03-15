import csv
import os

# Define the file where job applications will be saved
FILE_NAME = "job_applications.csv"

# Check if file exists, if not, create it with headers
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Company", "Job Title", "Date Applied", "Status"])

# Add a new job application
def add_job_application(company, job_title, date_applied, status):
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([company, job_title, date_applied, status])

# View all job applications
def view_all_applications():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Company: {row[0]}, Job Title: {row[1]}, Date Applied: {row[2]}, Status: {row[3]}")

# Update the status of a job application by its company name and job title
def update_status(company, job_title, new_status):
    rows = []
    updated = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        if row[0] == company and row[1] == job_title:
            row[3] = new_status
            updated = True

    if updated:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Status updated successfully.")
    else:
        print("Application not found.")

# Delete a job application by company and job title
def delete_application(company, job_title):
    rows = []
    deleted = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    rows = [row for row in rows if not (row[0] == company and row[1] == job_title)]

    if len(rows) < len(rows):
        deleted = True

    if deleted:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Application deleted successfully.")
    else:
        print("Application not found.")

# Main menu
def main_menu():
    while True:
        print("\nJob Application Tracker")
        print("1. Add New Job Application")
        print("2. see All Applications")
        print("3. Update Application Status")
        print("4. Delete Job Application")
        print("5. back")
        choice = input("Choose an option: ")

        if choice == '1':
            company = input("Enter the company name: ")
            job_title = input("Enter the job title: ")
            date_applied = input("Enter the date applied (YYYY-MM-DD): ")
            status = input("Enter the status (e.g., 'Applied', 'Interviewing', 'Rejected', 'Offered'): ")
            add_job_application(company, job_title, date_applied, status)
        elif choice == '2':
            print("\nAll Job Applications:")
            view_all_applications()
        elif choice == '3':
            company = input("Enter the company name: ")
            job_title = input("Enter the job title: ")
            new_status = input("Enter the new status: ")
            update_status(company, job_title, new_status)
        elif choice == '4':
            company = input("Enter the company name: ")
            job_title = input("Enter the job title: ")
            delete_application(company, job_title)
        elif choice == '5':
            print("Exiting Job Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    initialize_file()
    main_menu()