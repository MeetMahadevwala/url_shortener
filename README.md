# Python URL Shortener

<!-- 
A concise and descriptive title is the best way to start.
-->

![URL Shortener Demo](/img/test.png)
<!-- 
A screenshot or GIF of your application in action is highly effective. 
It immediately shows what the project does. You can create one and replace this placeholder.
-->

A full-featured URL Shortener web service built with Python and Flask. This application converts long, unwieldy URLs into short, manageable links and includes advanced features like custom aliases and click-tracking analytics.

---

## Features

<!-- 
This is your highlight reel. Use a bulleted list to clearly and concisely
showcase everything your application can do. This is great for quickly
informing recruiters or other developers of the project's scope.
-->
*   **Core URL Shortening:** Converts any long URL into a unique, random short code.
*   **Custom Aliases:** Users can provide their own custom alias for a branded, memorable short link.
*   **Click Tracking & Analytics:** Every click on a short link is counted, and a dedicated analytics page displays the total clicks, original URL, and more.
*   **RESTful API:** A well-defined API endpoint for programmatic URL shortening.
*   **Simple & Interactive Frontend:** A clean user interface built with HTML, CSS, and vanilla JavaScript that interacts with the backend API without page reloads.
*   **Robust Error Handling:** Custom, user-friendly pages for `404 Not Found` and `500 Internal Server` errors.

## Tech Stack

<!-- 
List the primary technologies you used. This gives a quick overview
of your technical skills.
-->
*   **Backend:** Python 3, Flask
*   **Database:** SQLite (via Flask-SQLAlchemy ORM)
*   **Frontend:** HTML5, CSS3, Vanilla JavaScript (with `fetch` API)
*   **Configuration:** `python-dotenv` for environment variable management

---

## Setup and Installation

<!-- 
This is the most critical section for other developers. These instructions
are a direct result of the professional setup you've done in the last few tasks
(creating a venv, requirements.txt, and .env file).
-->

To run this project locally, follow these steps:

### 1. Prerequisites

*   Python 3.8+
*   Git

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

### 3. Set Up and Run the Application
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
Create a .env file in the root directory with the following content:
```bash
# Generate your own secret key. You can use Python's `secrets` module.
# In a Python shell: import secrets; secrets.token_hex(24)
SECRET_KEY='YOUR_SUPER_SECRET_RANDOM_KEY_HERE'

# Database URI for development
SQLALCHEMY_DATABASE_URI='sqlite:///urls.db'
```
Initialize the database:
```bash
flask shell
```
Then in the Flask shell:
```bash
from app import db
db.create_all()
exit()
```
Alternatively, wrap db.create_all() inside with app.app_context(): in app.py and run it once.

Then in the Flask shell:
```bash
flask run
```
The app will be available at: http://127.0.0.1:5000
