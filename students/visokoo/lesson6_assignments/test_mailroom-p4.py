#!/usr/bin/env python3
"""
----------------------------------------------------
Assignment: test_mailroom-p4.py
Author: visokoo | Created: 2/15/2019
ChangeLog: 2/15/2019, Created pytest file

Pytest file for testing mailroom.py
----------------------------------------------------
"""
import pytest
import glob
from mailroom import thank_all, add_donation, donor_history

def test_add_donation_existing_donor():
  assert add_donation("Paul Allen", 45000) == 100000

def test_add_donation_new_donor():
  assert add_donation("James Cameron", 30000) == 30000

def test_add_donation_invalid_value():
  with pytest.raises(Exception):
    add_donation("Sansa Stark", "invalid value")

def test_send_letters_correct_count():
  thank_all()
  assert len(glob.glob("*.txt")) == 6

def test_send_letters_correct_content():
  thank_all()
  line_to_check = open("Mark_Zuckerberg.txt").readline()
  assert line_to_check == "Dear Mark, \n"

def test_donor_history_count_orig():
  assert donor_history("Mark Zuckerberg") == 3

def test_donor_history_count_edited():
  assert donor_history("Paul Allen") == 3