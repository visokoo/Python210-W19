#!/usr/bin/env python3
"""
----------------------------------------------------
Assignment: mailroom.py
Author: visokoo | Created: 2/1/2019
ChangeLog: 2/15/2019, Added unit testing

You work in the mail room at a local charity. Part of your job is to write incredibly boring,
repetitive emails thanking your donors for their generous gifts. You are tired of doing this
over and over again, so you’ve decided to let Python help you out of a jam and do your work for you.

Pt.3
- Add a full suite of unit tests.
----------------------------------------------------
"""

import re

donors = [
  {"name": "William Gates, III", "total_donation": 458978.00, "total_donation_count": 3},
  {"name": "Mark Zuckerberg", "total_donation": 54687.00, "total_donation_count": 2},
  {"name": "Jeff Bezos", "total_donation": 87485.50, "total_donation_count": 2},
  {"name": "Paul Allen", "total_donation": 55000.00, "total_donation_count": 1},
  {"name": "Arya Stark", "total_donation": 60000.00, "total_donation_count": 1}
]

def display_donors(donordb):
  [print(row) for row in donordb]

def find_donor(donor_name):
  for row in donors:
    if row["name"].lower() == donor_name.lower():
      return donor_name
  return donor_name

def thank_you():
  try:
    full_name = input("Name of the giftee (Enter 'list' if you want to see existing donors): ").title()
    if full_name == "List":
      display_donors(donors)
    else:
      donor_name = find_donor(full_name)
      donation_amount = input("Donation Amount: ")
      add_donation(donor_name, donation_amount)
      print(generate_email(donor_name, donation_amount))
  except ValueError:
    raise ValueError("The donation amount must be a number, try again.")

def thank_all():
  for row in donors:
    email = generate_email(row["name"], row["total_donation"])
    # replacing non-alphanumeric chars w/ "_"
    with open(f"{re.sub('[^a-zA-Z0-9_]', '_', row['name'])}.txt", "w") as file:
      file.write(email)
  print("Saved email templates to local directory as <donor_name>.txt")

def add_donation(donor_name, donation):
  donor_count = donor_history(donor_name)
  donation = float(donation)
  for row in donors:
    if row["name"].lower() == donor_name.lower():
      new_amount = row["total_donation"] + donation
      # remove old donor from list completely & insert again with new data
      row.clear()
      row.update({"name": donor_name, "total_donation": new_amount, "total_donation_count": donor_count})
      return new_amount
  else:
    donors.append({"name": donor_name, "total_donation": donation, "total_donation_count": donor_count})
    return donation

def donor_history(donor_name):
  for row in donors:
    if row["name"].lower() == donor_name.lower():
      return row["total_donation_count"] + 1
  return 1

def generate_email(donor_name, donation):
  email = "Dear {}, \n\nThank you so much for your generous donation amount of ${:.2f}.\n" \
          "Your help will directly benefit the thousands of starving families this winter.\n" \
          "Thank you again for making a difference in their lives.\n\n" \
          "Cheers,\n" \
          "A grateful volunteer".format(donor_name.split(' ')[0].capitalize(), float(donation))
  return email

def generate_report():
  sorted_donors = sorted(donors, key=lambda k: k["total_donation"], reverse=True)
  print("{:25}| {:^16} | {:^11} | {}".format("Donor Name",
                                             "Total Given",
                                             "Num Gifts",
                                             "Average Gift"),
                                             "-" * 72, sep="\n")

  for row in sorted_donors:
    print("{:25}| ${:>15.2f} | {:>11} | ${:11.2f}".format(row["name"],
                                                          row["total_donation"],
                                                          row["total_donation_count"],
                                                          row["total_donation"] / row["total_donation_count"]))
  print()

def display_menu():
  return ("Select an option:" + "\n" +
                   "1. Send a Thank You" + "\n" +
                   "2. Create a Report" + "\n" +
                   "3. Send a Thank You to everyone" + "\n" +
                   "4. Quit" + "\n")

def main():
  choice_options = {
    1: thank_you,
    2: generate_report,
    3: thank_all,
    4: quit
  }

  while True:
    print(display_menu())
    try:
      option = int(input("Choice: "))
      choice_options[option]()
    except KeyError:
      print("Invalid option. Please choose a choice that exist in the menu.")
    except Exception as e:
      print("Python reported this error: ", e)

if __name__ == '__main__':
  main()
# else: raise Exception("This file is not meant to be imported.")