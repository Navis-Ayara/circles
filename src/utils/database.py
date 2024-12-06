import json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

with open(f"{os.getenv("FLET_APP_STORAGE_DATA")}/database.json", "r") as database:
    db = json.load(database)

def create_user(username, email, profile_picture_url):
    user = {
        "username": username,
        "email": email,
        "profile_picture_url": profile_picture_url,
        "created_at": datetime.now().isoformat()
    }

    with open(f"{os.getenv("FLET_APP_STORAGE_DATA")}/database.json", "w") as database:
        db["users"][f"user_id_{len(db["users"])+1}"] = user
        json.dump(db, database, indent=4)

def get_user(id):
    return db["users"][id]

def get_user_id(email):
    for key, value in db["users"].items():
        if value["email"] == email:
            return key
        else:
            return False

def create_circle(name, description, owner_id, image_url):
    circle = {
        "name": name,
        "description": description,
        "owner_id": f"user_id_{owner_id}",
        "created_at": datetime.now().isoformat(),
        "image_url": image_url
    } 

    with open(f"{os.getenv("FLET_APP_STORAGE_DATA")}/database.json", "w") as database:
        
        db["circles"][f"circle_id_{len(db["circles"])+1}"] = circle
        json.dump(db, database, indent=4)

def get_circle_id(name):
    for key, value in db["circles"].items():
        if value["name"] == name:
            return key
        else:
            False

def get_circles(user_id=None):
    if not user_id:
        return db["circles"]
    else:
        my_circles = []
        for key, value in db["circles"].items():
            if value["owner_id"] == user_id:
                my_circles.append(
                    db["circles"][key]
                )
        for key, value in db["circle_members"].items():
            for _key, _value in db["circle_members"][key].items():
                if _key == user_id:
                    my_circles.append(
                        db["circles"][key]
                    )

        return my_circles

def update_circle(id, **kwargs):
    with open(f"{os.getenv("FLET_APP_STORAGE_DATA")}/database.json", "w") as database:
        if kwargs["name"]:
            circle_name = kwargs["name"]
            db["circles"][id]["circle_name"] = circle_name
        if kwargs["description"]:
            circle_description = kwargs["description"]
            db["circles"][id]["circle_description"] = circle_description
        json.dump(db, database, indent=4)

def join_circle(circle_id, user_id):
    with open(f"{os.getenv("FLET_APP_STORAGE_DATA")}/database.json", "w") as database:
        
        db["circle_members"] = {}
        db["circle_members"][circle_id] = {}
        db["circle_members"][circle_id][user_id] = {}
        db["circle_members"][circle_id][user_id]["joined_at"] = datetime.now().isoformat()
        json.dump(db)

def create_post(circle_id, user_id, content):
    post = {
        "circle_id": circle_id,
        "user_id": user_id,
        "content": content,
        "created_at": datetime.now().isoformat()
    }

    with open(f"{os.getenv("FLET_APP_STORAGE_DATA")}/database.json", ) as database:
        db = json.load(database.read())
        db["posts"][f"post_id_{len(db["posts"])+1}"] = post
        json.dump(db)

# def get_posts(user_id):
#     circles = get_circles(user_id)
#     posts = []

def create_comment(post_id, user_id, content):
    comment = {
        "post_id": post_id,
        "user_id": user_id,
        "content": content,
        "created_at": datetime.now().isoformat()
    }

    with open(f"{os.getenv("FLET_APP_STORAGE_DATA")}/database.json", "w") as database:
        
        db["comments"][f"comment_id_{len(db["comments"])+1}"] = comment
        json.dump(db)

# TODO: Implement cascade on user account deletion
