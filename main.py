import requests

def main():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/2")
    response_dict = response.json()
    print (f"Title: {response_dict["title"]}")
    print (f"Completed: {response_dict["completed"]}")
    print (f"User Id: {response_dict["userId"]}")


if __name__ == "__main__":
    main()
