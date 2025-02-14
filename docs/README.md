# Faceless Influencer Creation and Meme Posting Automation

This project automates the creation and management of "faceless" influencers on social media platforms like Instagram. It also includes meme scraping from Reddit and meme generation using AI models, with automated posting and scheduling.

## Features

- Automates Instagram account creation and profile management for faceless influencers.
- Scrapes memes from Reddit and other meme sources.
- Generates custom meme images and videos with captions.
- Automates meme posting to Instagram, including scheduling.
- Tracks basic post engagement metrics (likes, comments, etc.).

## Tech Stack

- **Backend**: Python (Flask)
- **Web Scraping**: BeautifulSoup, PRAW (Reddit API)
- **Meme Generation**: Pillow (image), FFmpeg (video)
- **Task Scheduling**: Celery, APScheduler
- **Database**: SQLite (for MVP)
- **Social Media Integration**: Instagram Graph API
- **Deployment**: Heroku or DigitalOcean

## Folder Structure

Here is the structure of the project folder:

```faceless-influencer-automation/
│
├── README.md                  # Project overview, setup instructions, and usage
├── .gitignore                 # Ignores unnecessary files (e.g., .env, virtualenv)
├── requirements.txt           # Lists all Python dependencies (generated via `pip freeze`)
├── Procfile                   # For Heroku deployment (if using Heroku)
├── Dockerfile                 # If using Docker to containerize your app (optional)
│
├── app/                        # Main application folder
│   ├── __init__.py             # Initializes the app package
│   ├── routes.py               # Flask route definitions (API endpoints)
│   ├── auth.py                 # Handles authentication (Instagram API OAuth)
│   ├── meme_scraper.py         # Logic for scraping memes from Reddit and other platforms
│   ├── meme_generator.py       # Handles meme image/video generation (Pillow/FFmpeg)
│   ├── scheduler.py            # Job scheduler setup (Celery or APScheduler)
│   ├── instagram_api.py        # Integrates Instagram Graph API (posting, media management)
│   ├── database.py             # Manages SQLite/PostgreSQL database connection and queries
│   └── config.py               # Configuration file (API keys, secrets, etc.)
│
├── tests/                      # Unit and integration tests
│   ├── test_routes.py           # Tests for routes
│   ├── test_auth.py             # Tests for authentication flow
│   ├── test_scraping.py         # Tests for meme scraping functionality
│   ├── test_meme_generator.py   # Tests for meme generation logic
│   └── test_instagram_api.py    # Tests for Instagram API integration
│
├── docs/                       # Documentation folder
│   ├── setup_guide.md          # Detailed setup instructions
│   ├── usage_guide.md          # How to use the app and contribute
│   └── api_documentation.md    # API endpoints documentation (if applicable)
│
└── .env                        # Environment variables (API keys, secrets) - ignored by .gitignore```
