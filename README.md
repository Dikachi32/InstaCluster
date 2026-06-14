# 🚀 InstaCluster: Instagram User Segmentation Engine

### 🎥 Watch the Live Demo

👉 https://www.linkedin.com/posts/dikachi-baron-a4a380356_machinelearning-artificialintelligence-datascience-ugcPost-7471926246449332225-WNX-/

---

## 📌 Project Overview

**InstaCluster** is an Unsupervised Machine Learning project that uses **K-Means Clustering** to segment Instagram users based on their behavior and spending patterns.

The system analyzes two key features:

* **Instagram Visit Score**
* **Spending Rank**

Using these features, the model automatically discovers hidden patterns and groups similar users into meaningful behavioral segments.

Unlike supervised learning, where models learn from both features and labels, this project uses **only features** and allows the model to identify patterns and create clusters on its own.

---

## 🎯 Project Goal

The primary goal of InstaCluster is to:

* Understand different categories of Instagram users.
* Identify highly engaged and low-engaged users.
* Discover high-value customers.
* Support targeted marketing strategies.
* Help businesses send the right offers to the right customers.

---

## 🧠 Why Unsupervised Learning?

### Supervised Learning

```
Features + Labels → Train Model → Prediction
```

### Unsupervised Learning

```
Features Only → Discover Patterns → Group Similar Users
```

This project demonstrates how machine learning can uncover hidden customer behaviors without predefined labels.

---

## 📊 Features Used

| Feature               | Description                                                |
| --------------------- | ---------------------------------------------------------- |
| Instagram Visit Score | Measures how frequently a user visits Instagram.           |
| Spending Rank         | Measures the user's spending behavior on a scale of 0–100. |

---

## 🔥 User Segments (5 Clusters)

The model identifies five different behavioral segments:

### 🟢 Cluster 1 – Casual Browser

Low visit frequency and low spending behavior.

### 🔵 Cluster 2 – Window Shopper

High browsing activity but limited spending.

### 🟡 Cluster 3 – High-Value Engager

Highly active users with strong spending patterns.

### 🟣 Cluster 4 – Passive Spender

Lower activity but relatively higher spending behavior.

### 🔴 Cluster 5 – Active Explorer

Users who frequently visit Instagram and actively engage with content.

---

## 🏗️ Project Pipeline

```text
Load Dataset
      ↓
Explore Data
      ↓
Feature Selection
      ↓
Standard Scaling
      ↓
Determine Optimal K (Elbow Method)
      ↓
Train K-Means Model
      ↓
Assign Cluster Labels
      ↓
Visualize Clusters
      ↓
Save Model & Scaler
      ↓
Deploy Web Application
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Joblib
* Flask
* HTML
* CSS

---

## 📂 Project Structure

```bash
INSTA/
│
├── app.py
├── insta_visit.ipynb
├── instagram_kmeans_model.pkl
├── instagram_scaler.pkl
├── instagram_visits_clustering.csv
│
├── templates/
│   └── insta.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/InstaCluster.git
cd InstaCluster
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open:

```bash
http://127.0.0.1:5000/
```

---

## 📸 Application Features

✅ Real-time user segmentation

✅ Predict behavioral segments instantly

✅ Confidence score generation

✅ Business insights for each cluster

✅ Cluster reference guide

✅ Interactive and responsive interface

---

## 💡 Business Applications

This project can be applied in:

* Customer Segmentation
* Digital Marketing
* Personalized Recommendations
* Customer Relationship Management
* E-commerce Analytics
* Social Media Analytics

---

## 📈 Example Prediction

**Input**

```text
Instagram Visit Score: 50
Spending Rank: 20
```

**Prediction**

```text
Cluster: Casual Browser
Confidence Score: 85.1%
```

---

## 🚀 Future Improvements

* Add more behavioral features.
* Deploy to the cloud.
* Integrate real Instagram analytics APIs.
* Add interactive dashboards.
* Support dynamic retraining.

---

## 👨‍💻 Developer

**Dikachi Baron**

Data Scientist | Machine Learning Engineer | AI Enthusiast

* LinkedIn: https://www.linkedin.com/in/dikachi-baron-a4a380356/
* GitHub: https://github.com/your-github-Dikachi32

---

## ⭐ Support

If you found this project useful, please consider giving it a **Star ⭐** on GitHub.

---

## 📜 License

This project is licensed under the MIT License.
