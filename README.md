

# Django E-Commerce Website

This is a fully functional e-commerce website built using the Django framework. The project includes features like product listings, cart management, checkout, and a responsive UI using Bootstrap.

## Features

- ✅ User Authentication (Login, Logout, Registration)
- ✅ Product Listing with Search and Pagination
- ✅ Shopping Cart Management
- ✅ Checkout System
- ✅ Admin Panel for Product Management
- ✅ Bootstrap for Responsive Design

## Technologies Used

- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default Django DB)
- **Version Control:** Git, GitHub

Project Structure

    ecomsite/
    ├── ecomsite/              # Project settings and configurations
    ├── products/              # Product app with models, views, and templates
    ├── templates/             # HTML templates for frontend
    ├── static/                # CSS, JS, and images
    ├── db.sqlite3             # Default SQLite database
    ├── manage.py              # Django management script
    ├── requirements.txt       # Project dependencies

Features Breakdown

Home Page
	•	Displays all available products with pagination.
	•	Search bar for product filtering.

Product Details Page
	•	Detailed view of each product with an “Add to Cart” button.

Cart Functionality
	•	Add and remove products from the cart.
	•	Real-time cart updates using JavaScript and localStorage.

Checkout Page
	•	Simple checkout system with total price calculation.

API Endpoints (Django REST Framework)
	•	GET /api/products/ – List all products
	•	GET /api/products/<id>/ – Product detail view
	•	POST /api/cart/ – Add item to cart
	•	GET /api/cart/ – View cart items
	•	POST /api/checkout/ – Process checkout

Contributing
	1.	Fork the repository.
	2.	Create a new branch: git checkout -b feature-branch.
	3.	Commit your changes: git commit -m 'Add new feature'.
	4.	Push to the branch: git push origin feature-branch.
	5.	Create a pull request.


This project is licensed under the MIT License.
Contact
•Author: Shani Chauhan
•Email: shanichauhan1542@gmail.com
•LinkedIn: https://www.linkedin.com/in/shani-chauhan-403789323/

