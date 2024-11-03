# Credit Card Fraud Detection System

### Project Overview
This project is a simple, efficient, and scalable Credit Card Fraud Detection System that predicts the likelihood of a transaction being fraudulent based on given transaction data. Using a trained model, the system evaluates each transaction’s attributes and classifies it as either potentially fraudulent or safe.

### Technologies Used

Below are the primary technologies and tools used to develop this project:

| Technology | Description | Logo |
|------------|-------------|------|
| **Python** | The core programming language used for building the backend, model training, and handling data. | ![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png) |
| **Flask** | A lightweight web framework in Python, used for creating the backend REST API. | ![Flask Logo](https://flask.palletsprojects.com/en/2.1.x/_images/flask-logo.png) |
| **Random Forest & XGBoost** | Machine learning models used for fraud detection. Random Forest provides high accuracy for initial classification, and XGBoost helps fine-tune and optimize the model further. | ![XGBoost Logo](https://upload.wikimedia.org/wikipedia/commons/6/69/XGBoost_logo.png) |
| **HTML/CSS/JavaScript** | These are used to create a simple and clean user interface for accepting user inputs and displaying prediction results. | ![HTML CSS JS Logos](https://upload.wikimedia.org/wikipedia/commons/3/38/HTML5_Badge.svg) |
| **GitHub** | Used for version control and hosting the code repository for collaborative development. | ![GitHub Logo](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png) |

---

### Project Structure

```plaintext
Credit Card Fraud Detection/
├── backend/
│   ├── app.py          
│   └── services/
│       └── model_service.py
│   ├── api/
│       └── routes.py
│   ├── frontend/
│       └── index.html                
│       └── styles.css                
│       └── script.js
│   └── models/
│       └── ensemble_model.pkl
│       └── scaler.pkl
│       └── threshold.pkl
├── datasets/
│    └── creditcard.csv       #Dataset
├── models/
│    └── model_train.py
│    └── preprocess.py
├── requirements.txt
├── README.md
```

---

### Model Training Steps

The machine learning model in this project was trained using the **Credit Card Fraud Detection Dataset**, which contains anonymized transaction data labeled as either fraudulent or legitimate. Below are the key steps to train the model:

1. **Data Loading**  
   The data (`creditcard.csv`) is loaded and preprocessed for the model training pipeline.

2. **Data Preprocessing**  
   - Check for any missing values and handle them appropriately.
   - Normalize or standardize features to bring them to a comparable scale.
   - Split the dataset into training and testing sets.

3. **Model Selection**  
   - **Random Forest** and **XGBoost** classifiers were selected due to their effectiveness in handling complex datasets and providing high accuracy in classification tasks.
   - The model is trained using the training dataset, and hyperparameter tuning is done to achieve optimal performance.

4. **Model Evaluation**  
   - After training, the model is evaluated using the testing set.
   - Key metrics such as accuracy, confusion matrix, and classification report (precision, recall, F1-score) are used to validate the model’s effectiveness.

5. **Model Saving**  
   - The trained model is saved as a `.pkl` file for easy loading and prediction in the Flask backend.

#### Running the Model Training Script

The `model_train.py` script handles the entire training process. To run the model training, execute the following command:

```bash
python model_train.py
```

---

### Backend API Endpoints

- **Base Endpoint (`/`)**  
  This endpoint serves as a welcome message to confirm the API is running.

- **Prediction Endpoint (`/predict`)**  
  This endpoint accepts JSON data with features `Time`, `V1` to `V28`, and `Amount`. The model returns a prediction along with a probability score indicating the likelihood of the transaction being fraudulent.

  Example JSON format:

  ```json
  {
      "Time": 406,
      "V1": -2.3122265423263,
      "V2": 1.95199201064158,
      ...
      "V28": -0.143275874698919,
      "Amount": 239.93
  }
  ```

  **Response**:
  
  ```json
  {
      "prediction": 1,
      "probability": 0.85
  }
  ```

---

### Frontend UI

The frontend consists of three primary files in the `/frontend` folder:

- **index.html**  
  Provides a user-friendly form to input individual transaction features or paste them collectively. It includes a button to parse comma-separated values into JSON format, which is then sent to the backend for prediction.

- **script.js**  
  JavaScript logic for handling form submission, parsing collective data, and displaying the prediction result.

- **styles.css**  
  Basic CSS styling for a simple and clean user interface.

---

### How to Run the Project

#### 1. Clone the Repository
```bash
git clone <repository-url>
cd project-directory
```

#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 3. Run the Backend Server
Start the Flask app with:
```bash
cd backend
python app.py
```
The server will run at `http://127.0.0.1:5000/`.

#### 4. Access the Frontend
Open `frontend/index.html` in a web browser to interact with the UI.

---

### Testing the System

1. **Run the Server**  
   Make sure the backend Flask server is running and ready to accept requests.

2. **Submit Test Data**  
   Use the frontend form to submit test data. Either enter each feature individually or paste a comma-separated list of values.

3. **View Prediction**  
   After submission, the prediction message will indicate whether there is a high likelihood of fraud based on the model’s evaluation.

---

### Future Enhancements

Potential improvements include:

- **Enhancing the UI/UX**: Incorporate advanced animations and dynamic feedback.
- **Model Upgrades**: Experiment with additional models or ensemble techniques to further improve prediction accuracy.
- **Feature Engineering**: Explore additional features or external data that may help improve model performance.

---
