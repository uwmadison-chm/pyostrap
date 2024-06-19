import os

from rest_adapter import RestAdapter

from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = os.getenv("BIOSTRAP_API_KEY")
    bio_api = RestAdapter(api_key=api_key)
    users_params = {"page": 1, "items_per_page": 1}
    response = bio_api.get("organizations/users", users_params)
    print(response)


if __name__ == "__main__":
    main()
