# SynthoMed

SynthoMed is a secure medical platform that protects patient privacy by utilizing synthetic data generation. It features a unique "Girly Medical" aesthetic and Role-Based Access Control (RBAC) for Admins, Doctors, and Researchers.

## Features
- **Synthetic Data Generation**: Uses `sdv` to generate privacy-preserving medical datasets based on real Kaggle data.
- **Role-Based Access**:
    - **Admins**: Full system access.
    - **Doctors**: Access to their own patients (real) and synthetic data.
    - **Researchers**: Access to synthetic data only.
- **Modern UI**: A clean, "girly" yet professional medical interface.

## Tech Stack
- **Backend**: Flask, SQLAlchemy, PostgreSQL
- **Frontend**: HTML5, CSS3 (Custom Design)
- **Data**: Pandas, SDV (Synthetic Data Vault), Kaggle API
- **Infrastructure**: Docker, Docker Compose

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/coursemer/SynthoMed.git
   cd SynthoMed
   ```

2. **Run with Docker**
   ```bash
   docker-compose up --build
   ```

3. **Initialize Database**
   (If not automatically handled)
   ```bash
   docker-compose exec web python init_db.py
   ```

4. **Access the App**
   Open [http://localhost:5000](http://localhost:5000)

## Default Credentials
- **Admin**: admin@synthomed.com / admin123
- **Doctor**: doctor@synthomed.com / doctor123
- **Researcher**: researcher@synthomed.com / researcher123
