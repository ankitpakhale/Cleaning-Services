# Project Washla - An E-commerce Platform for Convenient Cleaning Services

**Note: This project is for educational and demonstration purposes only. It is always recommended to review and enhance security measures when deploying an e-commerce website in a production environment.**

## Purpose

Project Washla is an e-commerce website built on Django that offers cleaning services. It provides a user-friendly interface for customers to browse and avail cleaning services. The website incorporates features such as user authentication, product management (add, update, and delete), a shopping cart system, a payment gateway powered by Razorpay, and the option for users to donate their payments.

## Installation

1. Clone the repository from GitHub:
   git clone https://github.com/ankitpakhale/Cleaning-Services

2. Change into the project directory:
   cd Cleaning-Services

3. Create a virtual environment:
   python -m venv venv

4. Activate the virtual environment:

- For Windows:
  ```
  venv\Scripts\activate
  ```
- For Unix or Linux:
  ```
  source venv/bin/activate
  ```

5. Install the required dependencies:
   pip install -r requirements.txt

6. Perform database migrations:
   python manage.py migrate

7. Run the development server:
   python manage.py runserver

8. Open your web browser and visit `http://localhost:8000` to access the website.

## Code Structure

The project follows a modular structure with separate apps for individual functionalities:

> **Note**: The project also includes a `base.html` file, which serves as the base template for the website. It contains common code elements such as the navigation bar and footer, providing consistency across different pages. This file is not associated with a specific app but is used as a reference template to extend and build upon in other templates.

- **signup**: This app handles user authentication, including user registration (signup), login/logout functionalities, password recovery, OTP generation through SMTP email, and new password creation.

- **categories**: This app manages the product catalog, allowing admin users to add, update, and delete products. It also handles displaying product details, such as name, description, price, and availability. Additionally, this app includes functionality related to payments, such as payment processing, order management, and transaction history.

- **calculator**: This app provides functionality for price calculation. It can be used to calculate the total cost of cleaning services based on various parameters, such as area size, type of service, and additional options.

- **app1**: This app is a general-purpose app for managing other pages of the website. It can handle creating, updating, and deleting pages such as About Us, Blogs, Testimonials, Contact, FAQs, Not Found 404, etc.

- *Other apps*: You can create additional apps as needed for other functionalities, such as shopping cart, payment gateway integration, and donation management.

## Features

### User Authentication

- Users can create an account, log in, and log out.
- User sessions are maintained to keep users authenticated across requests.

### Product Management

- Admin users have the ability to add, update, and delete products.
- Products are displayed with details such as name, description, price, and availability.

### Shopping Cart

- Users can add products to their shopping cart.
- They can view their cart, update the quantity of items, and remove products.
- The cart is persisted across sessions for registered users.

### Payment Gateway (Razorpay)

- Secure payment processing is enabled using the Razorpay payment gateway.
- Users can complete transactions using various payment methods supported by Razorpay.
- Payment status and details are displayed to the user after completing a transaction.

### Donation of Payment

- Users have the option to donate their payment to a cause supported by the website.
- Donations can be made during the payment process or separately through a dedicated donation page.
- Donation amounts are recorded and associated with the user's transaction history.

## Technology Stack

- Django: A high-level Python web framework that simplifies web development.
- Razorpay: A popular payment gateway service provider in India.
- HTML/CSS: Front-end markup and styling languages for building web pages.
- JavaScript: Programming language for adding interactivity and dynamic features.
- SQLite: Lightweight, file-based database used for development purposes (can be swapped with other databases for production).

## Contributors

- Ankit Pakhale (akp3067@gmail.com)

## License
This project is licensed under the [MIT License](LICENSE). Feel free to modify and use the code as per your requirements.

For more information, please refer to the [license file](LICENSE).

For questions or support, please contact [Ankit Pakhale](mailto:akp3067@gmail.com).
