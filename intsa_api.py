# import requests

# def get_facebook_profile(access_token):
#     url = f"https://graph.facebook.com/v17.0/me"
#     params = {
#         "fields": "id,name",
#         "access_token": access_token
#     }

#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         data = response.json()
#         print("User Profile Data:", data)
#     else:
#         print(f"Error {response.status_code}: {response.json()['error']['message']}")

# # Replace with your User Access Token
access_token = "EAARvvH51EJcBO40uAI2U3OsSdmBcdKdsF2c9GkV8BzN7R5g7xjnKZBvvX6utc9CzUMZBOZC0PZBoYIZCG4bIcP6V8rrWPfnf3GZAAFIWT9DEjjGhMLcM70K6yA8pRdltDDMn3jwrrlH2JvhO3C7m0tWnCqHKycdNyoc7tnFxfwJ3sa7PFdf8TZCOGdaQwfZBGP6SmZCO6J55Sl3ZC01UDSScThPMEXXGZAdfaN6W4ahco3F1oax1Dz4YrYgpwR3ugjjYKRRs2b5fQZDZD"

# get_facebook_profile(access_token)
import requests

def get_facebook_page_posts(page_id, access_token):
    url = f"https://graph.facebook.com/v17.0/{page_id}/posts"
    params = {
        "fields": "id,message,created_time",
        "access_token": access_token
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        posts = response.json().get('data', [])
        for post in posts:
            print(f"Post ID: {post['id']}\nMessage: {post.get('message', 'No message')}\n")
    else:
        print(f"Error {response.status_code}: {response.json()['error']['message']}")

# Replace with your Page ID and Access Token
page_id = "1746998949388396"

get_facebook_page_posts(page_id, access_token)
