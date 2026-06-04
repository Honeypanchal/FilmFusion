# 🎬 FilmFusion

FilmFusion is a full-stack movie and TV show discovery platform built using **React.js**, **Django REST Framework**, **PostgreSQL**, and **TMDB API**. Users can browse movies and TV shows, view details, search content, and explore trending entertainment data through a modern web interface.

## 🚀 Live Demo

### Frontend (Vercel)

https://film-fusion-seven.vercel.app

### Backend API (Render)

https://filmfusion-p4wa.onrender.com

---

## 📌 Features

* Browse Movies
* Browse TV Shows
* View Movie Details
* View TV Show Details
* Search Functionality
* TMDB Data Integration
* REST API Backend
* Responsive User Interface
* PostgreSQL Database Storage
* Cloud Deployment

---

## 🛠️ Tech Stack

### Frontend

* React.js
* React Router DOM
* Axios
* CSS3

### Backend

* Django
* Django REST Framework
* PostgreSQL
* WhiteNoise
* Gunicorn

### Deployment

* Vercel (Frontend)
* Render (Backend + PostgreSQL)

---

## 📂 Project Structure

```text
FilmFusion/
│
├── filmapp/                 # React Frontend
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── assets/
│   └── package.json
│
├── movies/                  # Django App
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── filmproject/             # Django Project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── movies_data.json
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## 🗄️ Database Models

### Movie

* tmdb_id
* title
* description
* release_date
* rating
* poster_path_w500
* poster_path_original
* backdrop_path_w500
* backdrop_path_original
* trailer_url
* genres

### TVShow

* tmdb_id
* name
* description
* first_air_date
* rating
* poster_path_w500
* poster_path_original
* backdrop_path_w500
* backdrop_path_original
* trailer_url
* genres

---

## 🔌 API Endpoints

### Get All Movies

```http
GET /api/movies/
```

### Get All TV Shows

```http
GET /api/tvshows/
```

### Get Combined Data

```http
GET /api/all/
```

---

## ⚙️ Local Installation

### Clone Repository

```bash
git clone https://github.com/Honeypanchal/FilmFusion.git
cd FilmFusion
```

### Backend Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend URL:

```text
http://127.0.0.1:8000
```

### Frontend Setup

```bash
cd filmapp
npm install
npm start
```

Frontend URL:

```text
http://localhost:3000
```

---

## 🌐 Environment Variables

Backend:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=your_postgresql_database_url
```

Frontend:

```env
REACT_APP_API_URL=https://filmfusion-p4wa.onrender.com
```

---

## 📸 Screenshots

### Home Page

* Movie Listings
* TV Show Listings
* Search Bar
* Navigation Menu

### Details Page

* Poster
* Description
* Rating
* Genres
* Trailer Link

---

## 📈 Future Enhancements

* User Authentication
* Favorites / Watchlist
* Reviews and Ratings
* Genre Filtering
* Pagination
* Recommendation System
* Dark Mode

---

## 👨‍💻 Author

**Honey Panchal**

GitHub:
https://github.com/Honeypanchal

---

## 📄 License

This project is created for educational and learning purposes.
