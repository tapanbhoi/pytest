import requests
import json
import logging
import configparser
config = configparser.ConfigParser()
config.read("config.ini")

# Extract the base URL from configuration
api_url = config.get("api", "base_url")
post_id = config.getint("api", "post_id")
output_filename = config.get("output", "filename")
def get_and_store_emails(post_id, output_filename):
    url = f"{api_url}?postId={post_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        comments = response.json()
        emails = [comment['email'] for comment in comments]

        with open(output_filename, "w") as f:
            for email in emails:
                f.write(email + "\n")

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    get_and_store_emails(post_id, output_filename)
