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

## ScreenShots
<img width="1908" height="896" alt="banner" src="https://github.com/user-attachments/assets/4ada3e83-4746-4571-b265-71d9c6563989" />
<img width="1910" height="889" alt="signup" src="https://github.com/user-attachments/assets/b76b2a68-f433-44a8-9cd0-a1671b18884e" />
<img width="1895" height="886" alt="signin" src="https://github.com/user-attachments/assets/036d85e7-8a96-46fd-9e9f-6893b979bd54" />
<img width="1901" height="894" alt="adminlogin" src="https://github.com/user-attachments/assets/4b0696f5-a15d-4248-90d4-33b2feb92438" />
<img width="1901" height="880" alt="adminoptions" src="https://github.com/user-attachments/assets/4cfaf6c6-4d5d-4c92-9e5b-5f2b43e3adc0" />
<img width="1902" height="886" alt="useroptions" src="https://github.com/user-attachments/assets/ab215433-00b9-4d8a-b09d-de64fae2fc00" />
<img width="1898" height="893" alt="cart" src="https://github.com/user-attachments/assets/0a1a6da0-05ea-4aeb-a91e-b2e831a40a30" />
<img width="1899" height="882" alt="paymentinterface" src="https://github.com/user-attachments/assets/4bc02275-523a-4527-b893-c0e9ea01359c" />


---

**Made with ❤️ by [Krishna Kishor](https://github.com/Kishor-2004)**
