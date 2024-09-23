import requests

def search_github(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.ok:
        data = response.json()
        
        # Display user details
        print(f"Name: {data.get('name', data['login'])}")
        print(f"Username: @{data['login']}")
        print(f"Bio: {data.get('bio', 'Account doesn\'t have a bio.')}")
        
        print("\nStats:")
        print(f"Public Repos: {data['public_repos']}")
        print(f"Followers: {data['followers']}")
        print(f"Following: {data['following']}")
        
        print("\nMedia:")
        print(f"Location: {data.get('location', 'Not Available')}")
        print(f"Blog: {data.get('blog', 'Not Available')}")
        print(f"Twitter: {data.get('twitter_username', 'Not Available')}")
        print(f"Company: {data.get('company', 'Not Available')}")
        
        # Display profile image URL
        print(f"\nProfile Image URL: {data['avatar_url']}")
        
    else:
        print(f"Error: {response.json().get('message')}")

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    search_github(username)
