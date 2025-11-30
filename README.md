# 📝 Postify - Modern Blogging Platform

<div align="center">

![Django](https://img.shields.io/badge/Django-5.2.7-092E20?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A feature-rich, production-ready blogging platform built with Django MVT architecture**

[Features](#-features) • [Architecture](#-architecture) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-endpoints)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Technical Stack](#-technical-stack)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Database Schema](#-database-schema)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

**Postify** is a comprehensive blogging platform that demonstrates professional Django development practices. The project showcases a complete MVT (Model-View-Template) implementation with advanced features including user authentication, rich markdown support, hierarchical commenting, and real-time analytics.

### 🎯 Project Goals

- Provide a scalable and maintainable blogging solution
- Demonstrate best practices in Django development
- Implement a clean, modern UI/UX
- Support markdown-based content creation
- Enable community engagement through comments and interactions

### 👨‍💻 Development Note

> **Backend Architecture**: All backend features, models, views, business logic, and database architecture were developed from scratch by [Abdulrahman Ramadan](https://github.com/ElDEEB21), showcasing expertise in Django framework and Python development.
>
> **Frontend Design**: The user interface and styling were generated with AI assistance to accelerate development, allowing focus on robust backend implementation.

---

## ✨ Key Features

### 🔐 **Authentication & User Management**
- Custom user registration and login system
- Profile management with avatar support (binary storage)
- User bio and metadata
- Session-based authentication with allauth integration

### 📝 **Content Management**
- Rich markdown editor for post creation
- Cover image support with binary storage
- Category and tag organization
- Auto-generated URL slugs
- Post archiving functionality
- View count tracking
- Automatic read time calculation

### 💬 **Interactive Comments**
- Hierarchical comment system (parent-child relationships)
- Nested replies support
- Real-time comment threads
- User attribution and timestamps

### 📊 **Dashboard & Analytics**
- Personal dashboard for content creators
- Post statistics (views, comments, engagement)
- Monthly publication trends with Chart.js visualization
- Quick access to recent posts
- Archive management

### 🎨 **Modern UI/UX**
- Responsive design (mobile, tablet, desktop)
- Clean, professional interface
- Blue and orange color palette
- Smooth animations and transitions
- Custom 404 and 500 error pages

### 🔍 **Content Discovery**
- Browse posts by category
- Filter by tags
- Search functionality
- Featured posts section
- Related posts recommendations

---

## 🛠 Technical Stack

### Backend
- **Framework**: Django 5.2.7
- **Language**: Python 3.x
- **ORM**: Django ORM (SQLite for development)
- **Authentication**: Django Allauth
- **Markdown Processing**: Python Markdown

### Frontend
- **Template Engine**: Django Templates (Jinja2-like)
- **Styling**: CSS3 with CSS Variables
- **JavaScript**: Vanilla JS (ES6+)
- **Charts**: Chart.js for analytics
- **Icons**: Emoji-based iconography

### Database
- **Development**: SQLite3
- **Production Ready**: PostgreSQL/MySQL compatible

### Environment
- **Configuration**: python-dotenv for environment variables
- **Static Files**: Django Static Files management
- **Media**: Binary field storage for images

---

## 🏗 Architecture

### MVT Pattern Implementation

```
┌─────────────────────────────────────────────────┐
│                   Client Request                │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│              URLs (Routing Layer)               │
│  - postify_project/urls.py                      │
│  - accounts/urls.py                             │
│  - blog/urls.py                                 │
│  - comments/urls.py                             │
│  - dashboard/urls.py                            │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│              Views (Business Logic)             │
│  - Function-based views                         │
│  - Form validation                              │
│  - Authentication checks                        │
│  - Database queries                             │
└─────────────────┬───────────────────────────────┘
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
┌───────────────┐   ┌───────────────┐
│    Models     │   │   Templates   │
│  (Database)   │   │   (Render)    │
├───────────────┤   ├───────────────┤
│ • Post        │   │ • base.html   │
│ • Category    │   │ • blog/       │
│ • Tag         │   │ • accounts/   │
│ • Comment     │   │ • dashboard/  │
│ • Profile     │   │ • components/ │
└───────────────┘   └───────────────┘
        │                   │
        └─────────┬─────────┘
                  ▼
┌─────────────────────────────────────────────────┐
│                 HTTP Response                   │
└─────────────────────────────────────────────────┘
```

### Application Structure

**Postify** is organized into five core Django apps:

1. **`core`** - Landing pages, static content (home, about, contact)
2. **`accounts`** - User authentication, profiles, registration
3. **`blog`** - Post management, categories, tags, CRUD operations
4. **`comments`** - Comment system with nested replies
5. **`dashboard`** - User analytics, post management, statistics

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ElDEEB21/postify-django.git
   cd postify-django
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key for cryptographic signing | Required |
| `DEBUG` | Debug mode (True/False) | `True` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `localhost,127.0.0.1` |

### Database Configuration

The project uses SQLite by default. To use PostgreSQL or MySQL:

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postify_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🚀 Usage

### Creating a Blog Post

1. Log in to your account
2. Navigate to **Dashboard** or click **Write** in the navbar
3. Fill in the post details:
   - **Title**: Your post title
   - **Excerpt**: Brief summary (max 200 chars)
   - **Content**: Full post content (Markdown supported)
   - **Cover Image**: Optional banner image
   - **Category**: Select a category
   - **Tags**: Choose relevant tags
4. Click **Publish**

### Markdown Support

Postify supports full Markdown syntax:

```markdown
# Heading 1
## Heading 2

**Bold text**
*Italic text*

[Link](https://example.com)
![Image](image-url)

- List item 1
- List item 2

> Blockquote

`inline code`

```python
# Code block
def hello():
    print("Hello, Postify!")
```
\`\`\`

### Managing Comments

- Users can comment on any published post
- Reply to comments to create nested threads
- Comments are displayed chronologically
- Only comment authors and admins can delete comments

---

## 📁 Project Structure

```
postify-django/
├── accounts/              # User authentication & profiles
│   ├── models.py         # Profile model
│   ├── views.py          # Login, register, profile views
│   ├── forms.py          # User forms
│   ├── urls.py           # Account routes
│   ├── templates/        # Account templates
│   └── static/           # Account-specific CSS/JS
│
├── blog/                  # Core blogging functionality
│   ├── models.py         # Post, Category, Tag models
│   ├── views.py          # CRUD operations for posts
│   ├── forms.py          # Post creation forms
│   ├── urls.py           # Blog routes
│   ├── templates/        # Blog templates
│   └── static/           # Blog-specific CSS/JS
│
├── comments/              # Comment system
│   ├── models.py         # Comment model with parent-child
│   ├── views.py          # Comment CRUD
│   ├── forms.py          # Comment forms
│   ├── urls.py           # Comment routes
│   └── templates/        # Comment templates
│
├── core/                  # Landing & static pages
│   ├── views.py          # Home, about, contact
│   ├── urls.py           # Core routes
│   ├── templates/        # Landing page templates
│   └── static/           # Core CSS/images
│
├── dashboard/             # User dashboard & analytics
│   ├── views.py          # Dashboard logic, statistics
│   ├── urls.py           # Dashboard routes
│   ├── templates/        # Dashboard templates
│   └── static/           # Dashboard CSS/JS (Chart.js)
│
├── postify_project/       # Project configuration
│   ├── settings.py       # Django settings
│   ├── urls.py           # Root URL configuration
│   ├── views.py          # Custom error handlers
│   ├── wsgi.py           # WSGI config
│   └── asgi.py           # ASGI config
│
├── static/                # Global static files
│   ├── app.css           # Global styles
│   └── components/       # Reusable components
│
├── templates/             # Global templates
│   ├── base.html         # Base template
│   ├── 404.html          # Custom 404 page
│   ├── 500.html          # Custom 500 page
│   └── components/       # Shared components
│
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .env                  # Environment variables (create this)
```

---

## 🗄 Database Schema

### Models Overview

#### **Post Model**
```python
- id (PK)
- author (FK → User)
- title (CharField)
- excerpt (TextField)
- content (TextField)
- slug (SlugField, unique)
- category (FK → Category)
- tags (M2M → Tag)
- cover_image (BinaryField)
- cover_image_type (CharField)
- views (PositiveIntegerField)
- is_archived (BooleanField)
- created_at (DateTimeField)
```

#### **Category Model**
```python
- id (PK)
- name (CharField)
```

#### **Tag Model**
```python
- id (PK)
- name (CharField)
```

#### **Comment Model**
```python
- id (PK)
- user (FK → User)
- post (FK → Post)
- parent (FK → Comment, nullable)
- content (TextField)
- created_at (DateTimeField)
```

#### **Profile Model**
```python
- id (PK)
- user (OneToOne → User)
- bio (TextField)
- avatar (BinaryField)
- avatar_type (CharField)
```

### Entity Relationship Diagram

```
┌─────────────┐
│    User     │
└──────┬──────┘
       │ 1
       │
       │ 1     ┌─────────────┐
       ├───────┤   Profile   │
       │       └─────────────┘
       │
       │ 1..* ┌─────────────┐
       ├──────┤    Post     │
       │      └──────┬──────┘
       │             │ M
       │ 1..*        │
       ├────────┐    │ M     ┌─────────────┐
       │        │    ├───────┤     Tag     │
       │        │    │       └─────────────┘
       │        │    │
       │        │    │ M     ┌─────────────┐
       │        │    └───────┤  Category   │
       │        │            └─────────────┘
       │        │
       │        │ 1..*
       │        └────────────┐
       │                     │
       │ 1..*                ▼
       └──────────────► ┌─────────────┐
                        │   Comment   │
                        └──────┬──────┘
                               │
                               │ self-referencing
                               └──────┐
                                      │
                                (parent-child)
```

---

## 🔌 API Endpoints

### Authentication
- `GET/POST /accounts/login/` - User login
- `GET/POST /accounts/register/` - User registration
- `POST /accounts/logout/` - User logout
- `GET/POST /accounts/profile/<username>/` - View/edit profile

### Blog
- `GET /` - Homepage with featured posts
- `GET /blog/` - All blog posts
- `GET /blog/<slug>/` - View single post
- `GET/POST /blog/write/` - Create new post (auth required)
- `GET/POST /blog/<slug>/edit/` - Edit post (auth + owner required)
- `POST /blog/<slug>/delete/` - Delete post (auth + owner required)

### Comments
- `POST /comments/<int:post_id>/add/` - Add comment (auth required)
- `POST /comments/<int:comment_id>/delete/` - Delete comment (auth required)

### Dashboard
- `GET /dashboard/` - User dashboard with statistics (auth required)

### Static Pages
- `GET /about/` - About page
- `GET /contact/` - Contact page

---

## 🎨 Customization

### Color Palette

The project uses CSS variables for easy theming:

```css
:root {
  --primary: #1E40AF;      /* Deep Blue */
  --secondary: #3B82F6;    /* Sky Blue */
  --accent: #F59E0B;       /* Orange */
  --bg: #F9FAFB;          /* Off-White */
  --text: #1F2937;        /* Dark Gray */
  --text-light: #4B5563;  /* Gray */
  --bg-card: #FFFFFF;     /* White */
  --border: #E5E7EB;      /* Light Gray */
  --success: #10B981;     /* Green */
  --error: #EF4444;       /* Red */
}
```

---

## 🧪 Testing

Run tests with:
```bash
python manage.py test
```

For coverage:
```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 📈 Future Enhancements

- [ ] RESTful API with Django REST Framework
- [ ] Social media authentication (Google, GitHub)
- [ ] Post scheduling
- [ ] Email notifications
- [ ] Advanced search with Elasticsearch
- [ ] Post drafts and revisions
- [ ] User roles (Admin, Editor, Author)
- [ ] Comment moderation
- [ ] RSS feed
- [ ] Sitemap generation
- [ ] SEO optimization

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👤 Author

**Abdulrahman Ramadan Abdulkareem Mohamed**

- GitHub: [@ElDEEB21](https://github.com/ElDEEB21)
- Email: ar2724@fayoum.edu.eg

---

## 🙏 Acknowledgments

- Django Documentation
- Chart.js for analytics visualization
- Python Markdown library
- The Django community

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star!**

Made with ❤️ and Django

</div>