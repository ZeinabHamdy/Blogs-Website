## Blogs Website (Django)  
A full-featured blogging platform built with Django, supporting user management, post publishing, and content sharing.

### Key Features:

✏️**Post Management (CRUD):** Users can create, update, and delete their own blog posts. Only the original author has permission to modify or remove a post.

📤 **Share via Email:** Readers can share blog posts with others via email.

📄 **Pagination:** Posts are paginated for better content navigation and user experience.

🔐 **User Authentication:** Includes login, logout, and user registration functionality.

🧑‍💼 **User Profile System:** Each user has a personal profile created automatically upon registration using Django signals. Users can view and edit their profiles.

📋 **Posts Visibility:**

- Users can view both published and draft posts they have written.  
- Other users can only view published posts.

📌 **Post Status Control:**  
Posts can be saved as either *draft* or *published*. Once a post is marked as *published*, it cannot be reverted back to *draft*.


**Project Images (Demo):**
![Home](project_images/Screenshot%201.jpg)
![Home](project_images/Screenshot%202.jpg)
![Home](project_images/Screenshot%203.jpg)
![Home](project_images/Screenshot%204.jpg)
![Home](project_images/Screenshot%205.jpg)
![Home](project_images/Screenshot%206.jpg)
![Home](project_images/Screenshot%207.jpg)
![Home](project_images/Screenshot%208.jpg)
![Home](project_images/Screenshot%209.jpg)
![Home](project_images/Screenshot%2010.jpg)
![Home](project_images/Screenshot%2011.jpg)


## Local Development Setup

Follow these steps to set up the Blogs Website project on your local machine:

### Prerequisites

- Python 3.8 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the repository

```bash
git clone https://github.com/ZeinabHamdy/Blogs-Website.git
cd django-blogs-website
```

### Step 2: Set up a virtual environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set up PostgreSQL database

1. Install PostgreSQL if you haven't already
2. Create a new PostgreSQL database:
   ```bash
   psql -U postgres
   CREATE DATABASE your_database_name;
   CREATE USER your_database_user WITH PASSWORD 'your_database_password';
   ALTER ROLE your_database_user SET client_encoding TO 'utf8';
   ALTER ROLE your_database_user SET default_transaction_isolation TO 'read committed';
   ALTER ROLE your_database_user SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_database_user;
   \q
   ```

### Step 5: Configure environment variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Open the `.env` file and update the following variables with your own values:
   - Database settings: `DB_NAME`, `DB_USER`, `DB_PASSWORD`
   - Email settings: `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`
   - Generate a Django secret key and set `SECRET_KEY`

### Step 6: Run migrations

```bash
python manage.py migrate
```

### Step 7: Create a superuser (admin)

```bash
python manage.py createsuperuser
```

### Step 8: Run the development server

```bash
python manage.py runserver
```

The application should now be running at http://127.0.0.1:8000/

### Step 9: Access the admin panel

Go to http://127.0.0.1:8000/admin/ and log in using the superuser credentials you created.

### Common Issues and Troubleshooting

1. **Database Connection Issues**: Make sure PostgreSQL is running and your database credentials are correct in the `.env` file.

2. **Missing Dependencies**: If you encounter module import errors, ensure all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

3. **Static Files Not Loading**: Run the collectstatic command:
   ```bash
   python manage.py collectstatic
   ```

4. **Email Sending Failures**: Check your email configuration in the `.env` file and make sure you've set up the correct SMTP settings.