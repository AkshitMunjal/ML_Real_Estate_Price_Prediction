
## 🏡ML Real Estate Price Prediction

This project predicts real estate prices using Machine Learning techniques. The dataset used is the Bangalore House Prices Dataset, and the model is deployed using Flask with a frontend built using HTML, CSS, and JavaScript. The API is tested with Postman.


## 📊Machine Learning Project Lifecycle

This project follows the standard ML project lifecycle:

✅Problem Definition - Predict real estate prices based on various factors.

✅Data Collection - Used Bangalore House Prices Dataset.

✅ Data Preprocessing - Cleaning and transforming the dataset.

✅ Feature Engineering - Selecting relevant features for model training.

✅ Model Training & Evaluation - Trained a Linear Regression Model.

✅ Model Deployment - Flask-based API to serve predictions.

✅ Frontend Integration - Built a UI using HTML, CSS, and JavaScript.
## 🔥Features

✅ Predicts house prices based on user input.

✅ Uses Linear Regression for price prediction.

✅ Flask API for backend processing.

✅ Frontend built with HTML, CSS, and JavaScript.

✅ Tested with Postman for API validation.
## 🛠 Tech Stack

👉Machine Learning: Python, Pandas, NumPy, Scikit-learn

👉Backend: Flask (API for predictions)

👉Frontend: HTML, CSS, JavaScript

👉Database: CSV (Bangalore House Prices Dataset)

👉Testing: Postman

👉Algorithm: Linear Regression


## 🚀 How to Run

1️⃣ Clone the Repository

git clone https://github.com/AkshitMunjal/ML_Real_Estate_Price_Prediction.git

cd ML_Real_Estate_Price_Prediction

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Flask API

python server/server.py

4️⃣ Access the Frontend

Open client/templates/app.html in your browser.

📬 API Endpoints

POST /predict - Predicts house prices based on input parameters.

Request:

    POST /predict
            {
                "area": 1500,
                "location": "Indira Nagar",
                "bhk": 3,
                "bath": 2
            }

    Response:
            {
                "estimated_price": 125.75
            }




## Screenshots

![Home Price Prediction Application](https://raw.githubusercontent.com/AkshitMunjal/ML_Real_Estate_Price_Prediction/main/Home_Price_Prediction_Application.png)

## 📊 Dataset Overview

📍 Name: Bangalore House Prices Dataset

📥 Source: Kaggle / Open-source

📌 Contains: Features like 🏠 area, 📍 location, 🛏️ BHK, 💰 price



🎯 Future Improvements

✅ 🔗 Database Integration: Store dynamic data for real-time predictions.

✅ 📈 Model Enhancement: Improve accuracy using advanced ML techniques.

✅ ☁️ Cloud Deployment: Host the app on AWS/GCP for better accessibility.
## Let’s Connect! 🤝

I’m always excited to collaborate on data-driven projects or join innovative teams 🚀. Let’s build something extraordinary together! 🌟

📧Email: akshitmunjal479@gmail.com

🔗LinkedIn: www.linkedin.com/in/akshit-munjal-81851b188

🌐Portfolio:https://padlet.com/akshitmunjal479/projects-portfolio-ozbg80dvuk6fl9gg