# RentalCoverInstantQuote
This is an automation script written in Python using the Selenium WebDriver to get an instant quote from the Rental Cover website.

Prerequisites
Python 3.x
Selenium WebDriver
Installation
Install Python 3.x
Install Selenium 

Usage
Clone the repository to your local machine
Open the terminal and navigate to the folder containing the script
Run the following command:
python RentalCoverInstantQuote.py

Code Structure
The script starts by importing the necessary libraries. Then, it sets up the webdriver to load the Rental Cover website.
In the test_get_instant_quote method, the script performs the following actions:

Waits for the "Accept" button to be present and clicks it
Selects the renting country as the United States
Selects the date range for renting
Changes the country of residence to the United States
Gets the instant quote by clicking the "Get Your Instant Quote" button

Note
The script uses the Chrome webdriver to automate the actions.
The script is set up to select a specific date range, but you can modify it to select a different date range if desired.
The script uses explicit waits to handle dynamic elements on the website.
