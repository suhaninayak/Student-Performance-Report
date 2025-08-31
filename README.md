# Student Performance Report (Tkinter + MySQL + Matplotlib)

This is a Python **Tkinter GUI project** that manages and analyzes student performance data. It uses **MySQL** for database storage and **Matplotlib** for visualization, along with CSV support for easy data import/export.

---

## 🚀 Features

* 🎓 Add, update, and delete student records
* 💾 Store and manage performance data in MySQL
* 📊 Generate charts and visualizations using Matplotlib
* 📂 Import and export data in CSV format
* 🖥️ User-friendly Tkinter GUI

---

## 🛠️ Technologies Used

* **Python** (Tkinter, CSV, Matplotlib)
* **MySQL** (Database)
* **CSV** (Data import/export)

---

## ▶️ How to Run

1. **Clone this repo:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/Student-Performance-Report.git
   cd Student-Performance-Report
   ```

2. **Install dependencies:**

   ```bash
   pip install matplotlib mysql-connector-python
   ```

3. **Set up MySQL Database:**
   Open MySQL and run the following commands:

   ```sql
   CREATE DATABASE MyProject;
   USE MyProject;

   CREATE TABLE Admin (
       UserName VARCHAR(50) UNIQUE NOT NULL,
       Password VARCHAR(100) NOT NULL
   );

   INSERT INTO Admin (UserName, Password) VALUES ('admin', 'admin@123');
   ```

4. **Run the app:**

   ```bash
   python main.py
   ```

---

## 📷 Screenshots
![alt text](images/Screenshot%202025-08-31%20194238.png) ![alt text](images/Screenshot%202025-08-31%20194312.png)


---


## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.
