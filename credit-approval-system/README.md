# Credit Approval System

This project is a fully Dockerized backend-based Credit Approval System built using Django Rest Framework and PostgreSQL. It allows for the ingestion of customer and loan data from Excel files and exposes REST APIs for various functionalities.

## Features

- Register new customers
- Check loan eligibility
- Create new loans
- View loan details and all customer loans

## Project Structure

```
credit-approval-system
├── backend
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── credit_approval
│   ├── customers
│   ├── loans
│   ├── ingestion
│   └── core
├── docker-compose.yml
├── .env
├── .gitignore
└── README.md
```

## Requirements

- Python 3.x
- Django
- Django Rest Framework
- PostgreSQL
- Docker
- Docker Compose

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd credit-approval-system
   ```

2. **Create a `.env` file:**
   Copy the `.env.example` to `.env` and fill in the required environment variables.

3. **Build and run the Docker containers:**
   ```
   docker-compose up --build
   ```

4. **Run migrations:**
   ```
   docker-compose exec backend python manage.py migrate
   ```

5. **Load initial data (if applicable):**
   You can use the custom management command to import data from Excel files:
   ```
   docker-compose exec backend python manage.py import_excel <path-to-excel-file>
   ```

## API Endpoints

- **Customer Registration:** `POST /api/customers/`
- **Check Loan Eligibility:** `GET /api/customers/<customer_id>/eligibility/`
- **Create New Loan:** `POST /api/loans/`
- **View Loan Details:** `GET /api/loans/<loan_id>/`
- **View All Customer Loans:** `GET /api/customers/<customer_id>/loans/`

## Testing

To run the tests, use the following command:
```
docker-compose exec backend python manage.py test
```

## License

This project is licensed under the MIT License.