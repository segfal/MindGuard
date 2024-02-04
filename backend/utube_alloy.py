from dotenv import load_dotenv
import re
import requests
import os
import psycopg2

def extract_video_id(url):
    match = re.search(r"youtube\.com\/watch\?v=([a-zA-Z0-9_-]+)", url)
    if match:
        return match.group(1)
    return None

def get_video_title(api_key, video_id):
    base_url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        'part': 'snippet',
        'id': video_id,
        'key': api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        title = data['items'][0]['snippet']['title']
        return title
    except (requests.RequestException, KeyError, IndexError) as e:
        print(f"Error: {e}")
        return None

def insert_into_alloydb(title):
    # Modify these values with your PostgreSQL database connection details
    db_params = {
        'host': 'your_database_host',
        'database': 'your_database_name',
        'user': 'your_database_user',
        'password': 'your_database_password',
    }

    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Assuming you have a table named 'youtube_videos' with a 'title' column
        cursor.execute("INSERT INTO youtube_videos (title) VALUES (%s);", (title,))
        
        conn.commit()
        print("Title inserted into AlloyDB successfully.")
    except psycopg2.Error as e:
        print(f"Error inserting into AlloyDB: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    api_key = os.environ.get("YOUTUBE_DATA_API")
    youtube_url = input("Enter the YouTube video URL: ")

    video_id = extract_video_id(youtube_url)

    if video_id:
        video_title = get_video_title(api_key, video_id)

        if video_title:
            print(f"The title of the video is: {video_title}")
            
            # Insert the title into AlloyDB
            insert_into_alloydb(video_title)
        else:
            print("Failed to fetch the video title.")
    else:
        print("Invalid YouTube video URL. Make sure it contains a valid video ID.")
