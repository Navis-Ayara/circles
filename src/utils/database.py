import json
import os
from datetime import datetime

def create_user(username, email, profile_picture_url):
    user = {
        "username": username,
        "email": email,
        "profile_picture_url": profile_picture_url,
        "created_at": datetime.now().isoformat()
    }

    with open(os.getenv("FLET_APP_STORAGE_DATA"), "w") as database:
        db = json.load(database)
        db["users"][f"user_id_{len(db["users"])+1}"] = user
        json.dump(db, database)

def update_user(id, username, profile_picture_url):
    with open(os.getenv("FLET_APP_STORAGE_DATA"), "w") as database:
        db = json.load(database)
        db["users"][f"user_id_{id}"]["username"] = username
        db["users"][f"user_id_{id}"]["profile_picture_url"] = profile_picture_url
        json.dump(db, database)

def create_circle(name, description, owner_id, image_url):
    circle = {
        "name": name,
        "description": description,
        "owner_id": f"user_id_{owner_id}",
        "created_at": datetime.now().isoformat(),
        "image_url": image_url
    } 

    with open(os.getenv("FLET_APP_STORAGE_DATA"), "w") as database:
        db = json.load(database)
        db["circles"][f"circle_id_{len(db["circles"])+1}"] = circle
        json.dump(db, database)

def update_circle(id, **kwargs):
    if kwargs["name"]:
        circle_name = kwargs["name"]
    
    if kwargs["description"]:
        circle_description = kwargs["description"]
    
    with open(os.getenv("FLET_APP_STORAGE_DATA"), "w") as database:
        db = json.load(database)
        db["circles"][f"circle_id_{id}"]["circle_name"] = circle_name
        db["circles"][f"circle_id_{id}"]["circle_description"] = circle_description
        json.dump(db, database)

def join_circle(circle_id, user_id):
    with open(os.getenv("FLET_APP_STORAGE_DATA"), "w") as database:
        db = json.load(database)
        db["circle_members"] = {}
        db["circle_members"][f"circle_id_{circle_id}"] = {}
        db["circle_members"][f"circle_id_{circle_id}"][f"user_id_{user_id}"] = {}
        db["circle_members"][f"circle_id_{circle_id}"][f"user_id_{user_id}"]["joined_at"] = datetime.now().isoformat()
        json.dump(db)

def create_post(circle_id, user_id, content):
    post = {
        "circle_id": circle_id,
        "user_id": user_id,
        "content": content,
        "created_at": datetime.now().isoformat()
    }

    with open(os.getenv("FLET_APP_STORAGE_DATA"), "w") as database:
        db = json.load(database)
        db["posts"][f"post_id_{len(db["posts"])+1}"] = post
        json.dump(db)

def create_comment(post_id, user_id, content):
    comment = {
        "post_id": post_id,
        "user_id": user_id,
        "content": content,
        "created_at": datetime.now().isoformat()
    }

    with open(os.getenv("FLET_APP_STORAGE_DATA"), "w") as database:
        db = json.load(database)
        db["comments"][f"comment_id_{len(db["comments"])+1}"] = comment
        json.dump(db)

# TODO: Implement cascade on user account deletion
