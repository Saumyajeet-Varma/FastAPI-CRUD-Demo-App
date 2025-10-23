# FastAPI CRUD Demo App

A simple **CRUD API** built with [FastAPI](https://fastapi.tiangolo.com/) that manages user data (ID, Name, Branch).  
This project demonstrates how to create, read, update, and delete (CRUD) records using FastAPI and Pydantic.

---

## 🚀 Features
- **GET /** → Welcome message  
- **GET /users** → Fetch all users  
- **POST /user/create** → Create a new user  
- **PUT /user/{user_id}** → Update user details  
- **DELETE /user/delete/{user_id}** → Delete a user  

---

## Installation & Setup

### Clone the repository

```bash
git clone https://github.com/saumyajeet-varma/fastapi-crud-demo-app.git
cd fastapi-crud-demo-app

```

### Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

```

### Install dependencies

```bash
pip install -r requirements.txt

```

### Run the FastAPI app

```bash
uvicorn app:app

```

## API Endpoints

| Method | Endpoint                 | Description         | Request Body Example                                    |
| ------ | ------------------------ | ------------------- | ------------------------------------------------------- |
| GET    | `/`                      | Welcome message     | -                                                       |
| GET    | `/users`                 | Get all users       | -                                                       |
| POST   | `/user/create`           | Create a new user   | `{ "id": 1, "name": "Samm", "branch": "CSE" }`         |
| PUT    | `/user/{user_id}`        | Update user details | `{ "id": 1, "name": "Samm", "branch": "CE" }` |
| DELETE | `/user/delete/{user_id}` | Delete a user       | -                                                       |

## Tech Stack

- FastAPI - Web framework
- Pydantic - Data validation
- Uvicorn - ASGI server

## Contributing

Pull requests are welcome! If you’d like to make major changes, please open an issue first to discuss your ideas.