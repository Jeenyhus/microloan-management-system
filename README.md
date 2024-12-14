# Microloan Management System

The **Microloan Management System** is a Django-based web application designed to streamline operations for microloan companies. The system supports a subscription model where companies pay per user. It simplifies loan management processes, including loan applications, approvals, repayments, and client management.

---

## Features

### Core Features
- **User Management**: Role-based user access for loan officers, managers, and administrators.
- **Client Management**: Store and manage client details such as contact information and loan history.
- **Loan Management**:
  - Loan application process.
  - Loan approval workflows.
  - Track loan disbursements and repayments.
- **Payment Integration**: Support for payment processing and tracking.
- **Subscription Management**: Multi-company support with a per-user subscription model.

### Additional Features
- Real-time notifications.
- Analytics dashboard with insights into loan portfolio performance.
- Comprehensive audit trails for transactions and user actions.

---

## Installation

Follow these steps to set up the project on your local machine:

### Prerequisites
- Python 3.8+
- Django 4.0+
- PostgreSQL (or any supported database backend)
- Git
- Virtual Environment (recommended)

### Steps

1. **Clone the Repository**
   ```bash
   git clone git@github.com:yourusername/microloan-management-system.git
   cd microloan-management-system
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the root directory and configure the following:
   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_URL=postgres://user:password@localhost:5432/microloan
   ```

5. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Run the Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   Open your browser and go to [http://localhost:8000](http://localhost:8000).

---

## Usage

### Admin Panel
- Superusers can log in to the admin panel to manage users, clients, and loans.
- URL: [http://localhost:8000/admin](http://localhost:8000/admin)

### Core Workflows
1. **User Management**
   - Admins can create, update, or delete users.
   - Assign roles such as Loan Officer, Manager, etc.

2. **Client Management**
   - Add clients and view loan history.

3. **Loan Management**
   - Process loan applications, approvals, and repayments.
   - Track disbursements and overdue loans.

4. **Subscription Management**
   - Manage company subscriptions via the admin panel.

---

## Deployment

For production, follow these additional steps:

1. **Set `DEBUG=False`** in the `.env` file.
2. **Collect Static Files**:
   ```bash
   python manage.py collectstatic
   ```
3. **Use a Production Server** like Gunicorn:
   ```bash
   gunicorn microloan_management.wsgi:application --bind 0.0.0.0:8000
   ```
4. **Set Up a Reverse Proxy** (e.g., Nginx or Apache) to serve the application.

---

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Description of feature"
   ```
4. Push to your fork and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For support or inquiries, please contact:
- **Dabwitso Mweemba**
- Email: [mweembadabwitso@gmail.com](mailto:mweembadabwitso@gmail.com)
- GitHub: [Dabwitso](https://github.com/Jeenyhus)
