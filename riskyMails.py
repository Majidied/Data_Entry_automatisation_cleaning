import pandas as pd

def extract_invalid_emails(input_file, output_file):
    try:
        # Load CSV file (handles different delimiters)
        df = pd.read_csv(input_file, encoding="ISO-8859-1")

        # Check the column names
        print("Columns found:", df.columns)

        # Ensure the "email" and "quality" columns exist
        if "email" not in df.columns or "quality" not in df.columns:
            print("⚠ Missing 'email' or 'quality' column in the CSV file.")
            return

        # Extract invalid emails (where "quality" is not 'good')
        invalid_emails = df[df["quality"] != "good"]["email"]

        # Save invalid emails to a text file
        invalid_emails.to_csv(output_file, index=False, header=False, encoding="utf-8")

        print(f"✅ Invalid emails saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_csv = input("Enter the path to the input CSV file: ")
# Strip quotes from input if present
input_csv = input_csv.strip('"\'')
output_txt = "invalid_emails.txt"
extract_invalid_emails(input_csv, output_txt)