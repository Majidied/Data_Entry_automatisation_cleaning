# Data Entry Automation and Cleaning

This project provides a set of Python utilities to automate data entry tasks and clean contact information for business leads. It focuses on email validation, data cleaning, and associated media management.

## Features

- **Email Validation**: Identify and extract invalid or risky email addresses from CSV reports
- **Data Cleaning**: Remove entries with invalid emails from contact lists
- **Name Formatting**: Automatically normalize names (capitalize first names, uppercase last names)
- **Video Management**: Download and organize video files associated with contacts

## Files Overview

- riskyMails.py: Extract invalid emails from quality verification reports
- cleanLead.py: Clean contact lists by removing invalid emails and formatting names
- video_download.py: Download videos associated with contacts
- LeaderJour.csv: Original contact dataset
- LeaderJour_Cleaned.csv: Contact list with invalid emails removed
- LeaderJour_Cleaned_Names.csv: Contact list with properly formatted names
- invalid_emails.txt: List of identified invalid emails

## Usage

### 1. Extract Invalid Emails

```bash
python riskyMails.py
# When prompted, enter the path to your email verification report CSV
```

### 2. Clean Contact Lists

```bash
python cleanLead.py
# This will process LeaderJour.csv using invalid_emails.txt and output cleaned files
```

### 3. Download Associated Videos

```bash
python video_download.py
# When prompted, enter the path to the CSV containing video URLs
```

## Requirements

- Python 3.x
- pandas
- requests

## Data Processing Flow

1. Email validation reports are processed with riskyMails.py
2. Invalid emails are stored in invalid_emails.txt
3. Contact data is cleaned with cleanLead.py to remove entries with invalid emails
4. Names are formatted according to standard conventions
5. Videos can be downloaded for valid contacts using video_download.py

## Output

- Cleaned CSV files with valid contacts
- Properly formatted names for all contacts
- Organized video files (stored in the videos/ directory)