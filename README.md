# Foodnest – Python Full Stack Food Delivery App
Foodnest is a full stack web application for ordering food online, built with Python on the backend and modern web technologies on the frontend.

## ✨ Features

- User registration and authentication for customers and admins
- Restaurant and menu management (CRUD operations)
- Search and filter food items by category, price, cuisine
- Shopping cart management and order checkout
- Order history and real-time status tracking
- Responsive design for desktop and mobile
- Admin dashboard for restaurant owners

## 🛠️ Tech Stack

- **Backend:** Python (Django/Flask)
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap
- **Database:** SQLite/MySQL/PostgreSQL
- **Deployment:** Docker ready
  
## 📁 Project Structure
```
Foodnest/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── static/               # CSS, JS, Images
├── templates/            # HTML templates
├── media/                # User uploaded files
└── foodnest/             # Main Django app
├── models.py         # Database models
├── views.py          # Request handlers
├── urls.py           # URL routing
└── admin.py          # Admin interface
```
## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip
- Git

### Installationgit clone https://github.com/Kishor-2004/Foodnest.git
```
cd Foodnest
python -m venv venv && source venv/bin/activate  # Linux/Macvenv\Scripts\activate  # Windowspip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserverVisit `http://127.0.0.1:8000/
```


## 📱 Demo Features

- **Customer:** Browse menu → Add to cart → Checkout → Track order
- **Admin:** Manage restaurants → Add/Edit menu → View orders → Update status

## 🔮 Future Enhancements

- Payment gateway integration (Razorpay/Stripe)
- Real-time notifications (WebSockets)
- User ratings & reviews
- Delivery tracking with maps
- Push notifications
- Multi-restaurant support

## 📄 License

MIT License - Feel free to use for learning and development purposes.

---

**Made with ❤️ by [Krishna Kishor](https://github.com/Kishor-2004)**
