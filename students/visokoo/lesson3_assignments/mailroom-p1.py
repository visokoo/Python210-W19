#!/usr/bin/env python3
'''
----------------------------------------------------
Assignment: mailroom.py
Author: visokoo | Created: 1/25/2019
ChangeLog: 1/25/2019, Created file

You work in the mail room at a local charity. Part of your job is to write incredibly boring,
repetitive emails thanking your donors for their generous gifts. You are tired of doing this
over and over again, so you’ve decided to let Python help you out of a jam and do your work for you.
----------------------------------------------------
'''

import sys

donors = [
  ["William Gates, III", 458978.00, 3],
  ["Mark Zuckerberg", 54687.00, 2],
  ["Jeff Bezos", 87485.50, 2],
  ["Paul Allen", 55000.00, 1],
  ["Arya Stark", 60000.00, 1]
]

def display_donors(donordb):
  for row in donordb:
    print(row[0])

def find_donor(donor_name):
  for row in donors:
    if row[0].lower() == donor_name.lower():
      return donor_name
  return donor_name

def add_donation(donor_name, donation):
  donor_count = donor_history(donor_name)
  for row in donors:
    if row[0].lower() == donor_name.lower():
      new_amount = row[1] + donation
      # remove old donor amount from list & insert new_amount
      row.pop(1)
      row.insert(1, new_amount)
      # remove old donor acount from list and insert new
      row.pop(2)
      row.insert(2, donor_count)
      return new_amount
  else:
    donors.append([donor_name, donation, donor_count])
    return donation

def donor_history(donor_name):
  for row in donors:
    if row[0].lower() == donor_name.lower():
      return row[2] + 1
  return 1

def generate_email(donor_name, donation, total_donation):
  print(f"\nDear {donor_name.split(' ')[0].capitalize()},\n\n"
        f"Thank you so much for your generous donation amount of ${donation:.2f}.\n"
        f"This donation brings your total donation amount to ${total_donation:.2f}.\n"
        f"Your help will directly benefit the thousands of starving families this winter.\n"
        f"Thank you again for making a difference in their lives.\n\n"
        f"Cheers,\n"
        f"A grateful volunteer\n")

def generate_report(donordb):
  sorted_donors = sorted(donordb, key=lambda r: r[1], reverse=True)
  print("{:25}| {:^16} | {:^11} | {}".format("Donor Name",
                                             "Total Given",
                                             "Num Gifts",
                                             "Average Gift"),
                                             "-" * 72, sep="\n")
  for row in sorted_donors:
    print("{:25}| ${:>15.2f} | {:>11} | ${:11.2f}".format(row[0], row[1], row[2], row[1] / row[2]))
  print()

def main():
  while True:
    option = int(input("Select an option:" + "\n" +
                   "1. Send a Thank You" + "\n" +
                   "2. Create a Report" + "\n" +
                   "3. Quit" + "\n" +
                   "Choice: "))
    if option == 1:
      full_name = input("Name of the giftee (Enter 'list' if you want to see existing donors): ").title()
      if full_name == "List":
        display_donors(donors)
        continue
      else:
        donor_name = find_donor(full_name)
        donation_amount = float(input("Donation Amount: "))
        total_donation_amount = add_donation(donor_name, donation_amount)
        generate_email(donor_name, donation_amount, total_donation_amount)
    elif option == 2:
      generate_report(donors)
    else:
      print("Quitting...")
      break

if __name__ == '__main__':
  main()