from datetime import datetime

def date_difference(date1, date2):
    date_format = "%Y-%m-%d"
    try:
        date1_obj = datetime.strptime(date1, date_format)
        date2_obj = datetime.strptime(date2, date_format)
        difference = abs(date1_obj - date2_obj).days
        return difference
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

if __name__ == "__main__":
    date1 = input("Enter the first date (YYYY-MM-DD): ")
    date2 = input("Enter the second date (YYYY-MM-DD): ")
    print("Difference in days:", date_difference(date1, date2))
