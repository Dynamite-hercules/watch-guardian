# The Watch Guardian ⌚✨

> A minimal, luxury e-commerce platform for curated timepieces. Built as a full-stack portfolio showcase emphasizing dynamic relational database schemas, modular UI components, and fluid responsive design layouts.

---

## 🚀 Core Features & Architecture

- **Relational Database Normalization:** Structured leveraging a clean `Brand` -> `Watch` one-to-many relationship mapping, avoiding messy string entries and optimizing data integrity.
- **Premium Editorial Visuals:** Implements a modern, luxurious typography scale using the _Playfair Display_ and _Montserrat_ font pairings, set against high-breathing space grid containers.
- **Interactive Context States:** Handcrafted UI animations including an instantaneous secondary profile layout toggle on product hover, dynamic side-cart sliding drawers, and fluid image-gallery thumbnail perspective swappers.
- **Full Viewport Fluidity:** Built completely mobile-first, compressing automatically from an elegant 4-column layout on Ultra-wide displays down to highly touch-accessible navigation grids on compact mobile screens.

## 🛠️ Tech Stack & Dependencies

- **Backend Engine:** Django (Python 3.13+)
- **Database Layer:** SQLite (Production-ready abstraction for relational query filtering)
- **Frontend UI Framework:** HTML5 + Tailwind CSS (Integrated dynamically for lightning-fast styling deployment)
- **Image Microprocessing Library:** Pillow

---

## 💻 Local Windows Installation Guide

To get this workspace configured and running on your local environment, follow these parameters:

1. Clone the Repository & Navigate In:

```cmd
   git clone [https://github.com/Dynamite-hercules/watch-guardian.git](https://github.com/Dynamite-hercules/watch-guardian.git)
   cd watch-guardian
```

2. Initialize & Trigger the Python Virtual Environment:
   python -m venv venv
   venv\Scripts\activate

3. Install Dependencies:
   pip install django pillow

4. Execute Database Migrations:
   python manage.py migrate

5. Spin Up the Development Server Engine:
   python manage.py runserver
   Open your browser and navigate directly to: http://127.0.0.1:8000/

## 🎨 Future Scaling Architecture Goals

- Complete integration of asynchronous AJAX filtering mechanics to swap brands instantly without a page reload.
- Setup full session-based state caching for anonymous visitor shopping carts before moving to secure checkout workflows.
