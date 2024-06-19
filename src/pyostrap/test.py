from datetime import date
import os

from dotenv import load_dotenv

from biostrap_api import BiostrapApi


def main():
    load_dotenv()
    api_key = os.getenv("BIOSTRAP_API_KEY")
    bio_api = BiostrapApi(api_key=api_key)

if __name__ == "__main__":
    main()
