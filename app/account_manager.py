from requests_oauthlib import OAuth2Session
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Load environment variables
load_dotenv(dotenv_path='project.env')

# Instagram OAuth credentials from project.env
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
AUTHORIZATION_URL = 'https://api.instagram.com/oauth/authorize'
TOKEN_URL = 'https://api.instagram.com/oauth/access_token'

# Database setup
DATABASE_URI = 'sqlite:///instagram_accounts.db'  # Use SQLite for simplicity
Base = declarative_base()
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


class InstagramAccount(Base):
    __tablename__ = 'instagram_accounts'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    access_token = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(engine)


# Function to authenticate and store access tokens for each account
def authenticate_instagram_account():
    instagram = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
    authorization_url, state = instagram.authorization_url(AUTHORIZATION_URL)
    print(f'Visit this URL to authenticate: {authorization_url}')

    # Manually copy the URL you get after authentication
    redirect_response = input('Paste the full redirect URL here: ')

    # Get access token
    instagram.fetch_token(TOKEN_URL, client_secret=CLIENT_SECRET, authorization_response=redirect_response)

    # Get user info (optional)
    user_info = instagram.get('https://graph.instagram.com/me?fields=id,username').json()
    print(f'Authenticated as {user_info["username"]}')

    # Save access token and username to the database
    session = Session()
    new_account = InstagramAccount(username=user_info['username'], access_token=instagram.token['access_token'])
    session.add(new_account)
    session.commit()

    print(f'Account {user_info["username"]} added to the database.')


# Function to post media using stored access tokens
def post_media_to_instagram(account_id, image_url, caption):
    session = Session()
    account = session.query(InstagramAccount).filter_by(id=account_id).first()

    if not account:
        print(f'Account with ID {account_id} not found.')
        return

    access_token = account.access_token
    url = f'https://graph.instagram.com/me/media'
    params = {
        'image_url': image_url,
        'caption': caption,
        'access_token': access_token
    }

    response = requests.post(url, params=params)
    if response.status_code == 200:
        print(f"Post successful for {account.username}")
    else:
        print(f"Error posting: {response.json()}")


if __name__ == '__main__':
    # Authenticate a new account
    authenticate_instagram_account()

    # Post media to a specific account (replace `account_id` with actual account ID)
    post_media_to_instagram(account_id=1, image_url='https://example.com/image.jpg', caption='Hello World!')
