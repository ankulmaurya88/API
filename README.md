# 🚀 Flask-Based API Projects Collection

Welcome to the **API Repository** by [Ankul Maurya](https://github.com/ankulmaurya88) — a unified collection of multiple RESTful APIs built using **Flask**, **Flask-SQLAlchemy**, and other Python tools. These APIs cover various domains such as student management, hospital operations, grocery inventory, machine learning deployments, and more.

---

## 📁 Projects Included

| Project Directory              | Description |
|-------------------------------|-------------|
| `Attendance/`                 | API to manage and record student/employee attendance. |
| `flask-api/myapp/`            | Base template for Flask APIs with modular structure and SQLAlchemy integration. |
| `grocery_management_system/`  | API to manage grocery items, categories, stock, and billing. |
| `hospital-manegemets-api/`    | Hospital management API handling doctors, patients, appointments, and staff. |
| `house_price_API/`            | Machine Learning-powered API to predict house prices based on various features. |
| `ml_model_deployment_API/`    | General-purpose API for deploying machine learning models via Flask. |
| `student-manegment-api/`      | Full-featured API to manage student records, roles, and attendance with JWT authentication. |

---

## 🛠 Tech Stack

All APIs are built using the following stack:

- 🐍 **Python 3.8+**
- 🌐 **Flask** (for API development)
- 🗃️ **Flask-SQLAlchemy** (ORM for relational databases)
- 🔐 **Flask-JWT-Extended** (for token-based auth)
- 🧠 **Scikit-learn / Pandas** (for ML APIs)
- 🗂️ **Modular project structure**
- 🧪 **Postman / Swagger** (for API testing)

---

## 📂 Repository Structure

```plaintext
API/
├── Attendance/
├── flask-api/
│   └── myapp/
├── grocery_management_system/
├── hospital-manegemets-api/
├── house_price_API/
├── ml_model_deployment_API/
├── student-manegment-api/
└── README.md




## 🚀 How to Run Any API Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/ankulmaurya88/API.git
cd API
```

### Step 2: Navigate to the Target Project

```bash
cd student-manegment-api  # Change to any project folder
```

### Step 3: Create a Virtual Environment & Activate

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Flask Application

```bash
python app.py   # or python main.py depending on project
```

Your API will be available at:
http://127.0.0.1:5000/ or http://127.0.0.1:8000/

---

## 🔑 JWT Authentication (If Required)

Some APIs use JWT for authentication and role-based access control.

### Example Token Payload

```json
{
  "id": 1,
  "role": "admin"
}
```

### How to Use

Pass the token in your request headers:

```http
Authorization: Bearer <your_token_here>
```

---

## 📊 Example: House Price Prediction API

- **URL:** `/predict`
- **Method:** `POST`

### 📨 Request Body

```json
{
  "area": 2200,
  "bedrooms": 3,
  "bathrooms": 2,
  "location": "Banashankari"
}
```

### 📤 Response

```json
{
  "predicted_price": "₹92.5 Lakhs"
}
```

---

## 💡 Use Cases

- 🧑‍🎓 Manage student registration, attendance, and profiles
- 🏥 Handle hospital workflows like appointments and patient info
- 🛒 Manage inventory in grocery stores
- 🏠 Predict house prices using ML models
- 🤖 Deploy ML models using a Flask-based interface

---

## 📬 Contact

**Author:** Ankul Maurya  
📧 Email: ankulmaurya88@gmail.com  
🔗 GitHub: [ankulmaurya88](https://github.com/ankulmaurya88)
