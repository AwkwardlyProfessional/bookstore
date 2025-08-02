# 📚 Book Inventory REST API with Flask

This is a simple RESTful API built with **Flask** and **SQLite** to manage a collection of books. It supports basic CRUD operations with input validations and error handling.

---

## 🚀 Features

- 📖 Get all books: `GET /books`
- ➕ Add a new book: `POST /books`
- 🔍 Get book by ID: `GET /books/<id>`
- ✏️ Update a book: `PUT /books/<id>`
- ❌ Delete a book: `DELETE /books/<id>`

---

## 🧱 Book Model

Each book has the following fields:

| Field     | Type    | Description                     |
|-----------|---------|---------------------------------|
| id        | Integer | Auto-incremented primary key    |
| title     | String  | Title of the book (Required)    |
| author    | String  | Author of the book (Required)   |
| price     | Float   | Must be a positive value        |
| in_stock  | Boolean | Availability status             |

---

## ✅ Validations

- Title and Author must **not** be empty.
- Price must be a **positive float**.
- Proper **404 Not Found** and **400 Bad Request** error handling.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/book-inventory-api.git
cd book-inventory-api
