# Leaf Disease Detection System

## Project Description

The **Leaf Disease Detection System** is a web application that accepts an image input from the user (`.png`, `.jpg`, etc.) and feeds it to a trained `.h5` model. The model is trained on 30+ classes and predicts the output class. The prediction result, along with the detected class and its corresponding suggestion, is sent to the frontend and displayed to the user.

---

## Project Structure

```text
leaf-disease-detection/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── .env
│
├── backend/
│   ├── main.py
│   ├── model/
│   │   └── plant_disease_model.h5
│   └── requirements.txt
│
└── README.md
```

---

## Frontend

* The frontend is developed using **React**.
* Different endpoints are used for different functionalities.
* For example, image uploading uses one endpoint, while sending the image to the model uses another endpoint.
* Instead of using a single endpoint such as `localhost:5000`, multiple endpoints are used for better separation of functionality.
* All endpoints are accessed through environment variables stored in the `.env` file.
* The frontend is connected to the backend using **FastAPI (Python)**.

---

## UI/UX Design

### 1. Home Page

#### Hero Section

🌿 **Leaf Disease Detection System**

Upload a leaf image and get instant disease detection powered by Artificial Intelligence.

**Buttons:**

* Upload Image
* Learn More

#### Features Section

* 🔍 Disease Detection
* 🧠 AI-Powered Analysis
* 💡 Treatment Suggestions
* ⚡ Fast Prediction

#### How It Works

1. Upload Leaf Image
2. AI Analyzes the Image
3. Disease Identified
4. View Suggestion

---

### 2. Prediction Page

#### Left Side

**Image Upload Card**

```text
+----------------------+
| Upload Leaf Image    |
|                      |
|   Drag & Drop Here   |
|                      |
|   Choose File        |
+----------------------+
```

After uploading:

```text
+----------------------+
| Leaf Preview         |
|                      |
|      [ IMAGE ]       |
|                      |
+----------------------+
```

**Button**

```text
[ Predict Disease ]
```

#### Right Side

**Result Card**

```text
+------------------------------+
| Prediction Result            |
+------------------------------+
| Disease: Tomato Late Blight  |
| Confidence: 98.4%            |
+------------------------------+
```

**Suggestion:**

Apply fungicide and remove infected leaves.

**Status:**

⚠ Disease Detected

**Additional Components**

* Confidence Progress Bar
* Disease Severity Badge

Example:

```text
Confidence
[█████████████] 98%

Severity
[ Moderate ]
```

---

### 3. About Page

#### Project Information

**Leaf Disease Detection System**

**Technologies Used:**

* React
* FastAPI
* TensorFlow
* Keras (.h5)

**Supported Classes:**

* 38 Plant Disease Classes

#### Architecture

```text
User
 ↓
React Frontend
 ↓
FastAPI Backend
 ↓
TensorFlow Model
 ↓
Prediction
 ↓
Suggestion
```

---

## Color Palette

Use an agriculture-themed color scheme:

```text
Primary   : #2E7D32
Secondary : #4CAF50
Background: #F5FFF5
Text      : #1B1B1B
Success   : #2E7D32
Warning   : #FF9800
Error     : #D32F2F
```

---

## Backend

* The backend is developed using **FastAPI** and **Uvicorn**.
* It receives image inputs (`.png`, `.jpg`, etc.) from the frontend.
* The image is passed to the trained `.h5` model.
* The model predicts the output class based on the input image.

### Available Classes

(Use the following class mapping exactly as provided.)

```python
{0: 'Apple___Apple_scab',
1: 'Apple___Black_rot',
2: 'Apple___Cedar_apple_rust',
3: 'Apple___healthy',
4: 'Blueberry___healthy',
5: 'Cherry_(including_sour)___Powdery_mildew',
6: 'Cherry_(including_sour)___healthy',
7: 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
8: 'Corn_(maize)___Common_rust_',
9: 'Corn_(maize)___Northern_Leaf_Blight',
10: 'Corn_(maize)___healthy',
11: 'Grape___Black_rot',
12: 'Grape___Esca_(Black_Measles)',
13: 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
14: 'Grape___healthy',
15: 'Orange___Haunglongbing_(Citrus_greening)',
16: 'Peach___Bacterial_spot',
17: 'Peach___healthy',
18: 'Pepper,_bell___Bacterial_spot',
19: 'Pepper,_bell___healthy',
20: 'Potato___Early_blight',
21: 'Potato___Late_blight',
22: 'Potato___healthy',
23: 'Raspberry___healthy',
24: 'Soybean___healthy',
25: 'Squash___Powdery_mildew',
26: 'Strawberry___Leaf_scorch',
27: 'Strawberry___healthy',
28: 'Tomato___Bacterial_spot',
29: 'Tomato___Early_blight',
30: 'Tomato___Late_blight',
31: 'Tomato___Leaf_Mold',
32: 'Tomato___Septoria_leaf_spot',
33: 'Tomato___Spider_mites Two-spotted_spider_mite',
34: 'Tomato___Target_Spot',
35: 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
36: 'Tomato___Tomato_mosaic_virus',
37: 'Tomato___healthy'}
```

* Suggestions are stored in a Python dictionary.
* The dictionary contains mock suggestion data for all 38 classes.
* The final prediction result is sent to the frontend using FastAPI through different API endpoints for different features.

---

## Architecture Diagram

```text
User
│
▼
React Frontend
│
▼
FastAPI Backend
│
▼
TensorFlow .h5 Model
│
▼
Prediction Result
│
▼
Disease Suggestion
```
