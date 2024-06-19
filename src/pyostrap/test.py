import os

from dotenv import load_dotenv

from rest_adapter import RestAdapter
from models import User

def main():
    load_dotenv()
    api_key = os.getenv("BIOSTRAP_API_KEY")
    bio_api = RestAdapter(api_key=api_key)
    users_params = {"page": 1, "items_per_page": 1}
    response = bio_api.get("organizations/users", users_params)
    user = User(**response.data['users'][0])
    print(user.goals)
    

if __name__ == "__main__":
    main()
