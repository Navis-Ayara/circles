import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

from flet.auth.providers import GoogleOAuthProvider

provider = GoogleOAuthProvider(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_url="http://localhost:8550/oauth_callback"
)