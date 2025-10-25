import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
USERS_URL = f"{BASE_URL}/users"
TODOS_URL = f"{BASE_URL}/todos"


def get_all_users():
    response = requests.get(USERS_URL)
    #print(response)
    users = response.json()
    for user in users:
        print(user['name'])

def make_api_calls():
    get_all_users()
    


if __name__ == "__main__":
    make_api_calls()