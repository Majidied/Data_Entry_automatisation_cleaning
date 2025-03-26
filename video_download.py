import os
import csv
import shutil
import requests

def download_video(owner_full_name, url, output_folder , i):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            filename = os.path.join(output_folder, f"{owner_full_name}.mp4")
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Video downloaded {i}: {filename}")
        else:
            print(f"Failed to download: {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def extract_data_from_csv(file_path):
    data = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            email = row.get("email") or row.get("Owner(s) Email")  # Adjust for column names
            video_url = row.get("videoFileUrl")
            if email and video_url:
                data[email] = video_url
    return data

def extract_names_from_csv(file_path):
    names = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            owner_full_name = row.get("Owner Full name")
            email = row.get("Owner(s) Email")
            if owner_full_name and email:
                names[email] = owner_full_name
    return names

def download_videos(csv_video_file, csv_owner_file, output_folder):
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    
    os.makedirs(output_folder)
    video_data = extract_data_from_csv(csv_video_file)
    owner_names = extract_names_from_csv(csv_owner_file)
    i = 0
    
    for email, video_url in video_data.items():
        i += 1
        owner_name = owner_names.get(email, "Unknown")
        download_video(owner_name, video_url, output_folder , i)

if __name__ == "__main__":
    csv_video_file = input("Enter the path to the CSV file containing video URLs: ")  # CSV file containing video URLs
    csv_video_file = csv_video_file.strip('"\'')
    # csv_owner_file = input("Enter the path to the CSV file containing owner names: ")  # CSV file containing owner names
    # csv_owner_file = csv_owner_file.strip('"\'')
    csv_owner_file = "LeaderJour_Cleaned_Names.csv"
    output_folder = "videos"  # Output folder for downloaded videos
    
    download_videos(csv_video_file, csv_owner_file, output_folder)