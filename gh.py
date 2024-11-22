"""
=========================
Google Sheet Handler
=========================

**Do not modify the code** in this file.
"""

import gspread
from keys import gs_link, google_sheet
from all_students import student_scores

# Authenticate using the service account credentials from the 'credentials.json' file
gs = gspread.service_account(filename="credentials.json")
# Open the Google Sheet using its unique link (gs_link).
sh = gs.open_by_key(gs_link)

# Access the worksheet section named "RQ15" from the opened Google Sheet and store it in the 'worksheet' variable.
worksheet = sh.worksheet(google_sheet)

# Retrieve all the values from the worksheet and store them in the 'data' variable as a list of lists,
# where each inner list represents a row from the worksheet.
data = worksheet.get_all_values()

# Storing each student's score in a list of dictionaries, where each dictionary contains a student's name as the key
# and their score as the value.
for row in range(1, len(data)):
    for student in range(len(student_scores)):
        for j in student_scores[student]:
            if data[row][1].lower() in j.lower():
                student_scores[student][j] = data[row][5]


def main():
    # The list that contains students names and scores in dictionary
    # print(student_scores)

    # To check scores were stored correctly
    for student_dictionary in student_scores:
        for student_name in student_dictionary:
            print(f"{student_name}: {student_dictionary[student_name]}")


if __name__ == "__main__":
    main()
