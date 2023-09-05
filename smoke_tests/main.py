# pip install selenium
# get the gecko driver for your platform from https://github.com/mozilla/geckodriver/releases
import unittest
import argparse
import global_variables
from login_test import LoginTest
from specimen_test import SpecimenTest
from registerpatient import RegisterPatientTest

url_opt_short = "u"
url_opt_long = "url"
short_options = [url_opt_short]
long_options = [url_opt_long]

def main():
    parser = argparse.ArgumentParser(prog='main.py', description='Tests for BLIS')
    parser.add_argument("-u", "--url")
    args = parser.parse_args()
    url = args.url
    global_variables.blis_url = url

    suite = unittest.TestSuite()
    suite.addTest(LoginTest())
    suite.addTest(SpecimenTest())
    suite.addTest(RegisterPatientTest())

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    main()