import pandas as pd

def clean_invalid_emails(leader_file, invalid_emails_file, output_file):
    try:
        df = pd.read_csv(leader_file, delimiter=";", encoding="latin1")
        
        # Print column names to check for mismatches
        print("Column names:", df.columns)
        
        # Load invalid emails
        with open(invalid_emails_file, 'r', encoding="utf-8") as f:
            invalid_emails = set(line.strip() for line in f)
        
        # Strip spaces from column names
        df.columns = df.columns.str.strip()
        
        # Check for correct column name
        email_column = "Owner(s) Email"
        if email_column in df.columns:
            # Perform the cleaning
            df_cleaned = df[~df[email_column].isin(invalid_emails)]
            
            # Save using UTF-8 with BOM (utf-8-sig) to ensure French characters display correctly
            df_cleaned.to_csv(output_file, index=False, encoding="utf-8-sig", sep=";", quoting=1)
            
            print(f"✅ Cleaned file saved as {output_file}")
            print(f"Removed {len(df) - len(df_cleaned)} entries with invalid emails.")
        else:
            print("⚠ Column 'Owner(s) Email' not found. Check printed column names.")
    
    except Exception as e:
        print(f"Error: {e}")
        
def FixNames(input_file, output_file):
    """
    This function will fix the names of the columns in the CSV file.
    Expected columns: 'Owner Full name'; 'First'; 'Last'
    
    - The 'First' name will be modified so the first letter is capitalized and the rest lower case.
    - The 'Last' name will be entirely upper case.
    - The 'Owner Full name' will be re-created as "First Last".
    """
    try:
        df = pd.read_csv(input_file, delimiter=";", encoding="utf-8-sig")
        
        # Ensure the necessary columns exist
        if 'First' not in df.columns or 'Last' not in df.columns:
            print("⚠ Missing 'First' or 'Last' column. Cannot fix names.")
            return
        
        # Fix the first names: first letter capitalized, rest lower case
        df['First'] = df['First'].str.capitalize()
        
        # Fix the last names: all letters upper case
        df['Last'] = df['Last'].str.upper()
        
        # Create/Update the "Owner Full name" column as a combination of the fixed first and last names
        df['Owner Full name'] = df['First'] + " " + df['Last']
        
        # Save the updated file
        df.to_csv(output_file, index=False, encoding="utf-8-sig", sep=";")
        print(f"✅ Names fixed. Output saved to {output_file}")
    except Exception as e:
        print(f"Error in FixNames: {e}")



# Example usage
clean_invalid_emails("LeaderJour.csv", "invalid_emails.txt", "LeaderJour_Cleaned.csv")
FixNames("LeaderJour_Cleaned.csv", "LeaderJour_Cleaned_Names.csv")