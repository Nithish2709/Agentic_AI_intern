# Leaf Disease Detection System - Setup Guide

## Project Overview
The Leaf Disease Detection System is a full-stack web application that uses AI to identify plant diseases from leaf images. It features a React frontend for user interaction and a FastAPI backend for image processing and disease prediction.

## Project Structure
```
leaf-disease-detection/
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── HomePage.jsx
│   │   │   ├── HomePage.css
│   │   │   ├── PredictionPage.jsx
│   │   │   ├── PredictionPage.css
│   │   │   ├── AboutPage.jsx
│   │   │   └── AboutPage.css
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── main.jsx
│   │   └── index.css
│   ├── public/
│   ├── index.html
│   ├── vite.config.js
│   ├── package.json
│   └── .env
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── model/
│       └── plant_disease_model.h5 (to be added)
└── README.md
```

## Prerequisites
- Python 3.8+ (for backend)
- Node.js 16+ and npm (for frontend)
- Git

## Backend Setup

### 1. Create Python Environment
```bash
# Navigate to backend directory
cd leaf-disease-detection/backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Backend Server
```bash
python main.py
```

The backend will run on `http://localhost:8000`

### 4. Test Backend
- API Documentation: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/health`

## Frontend Setup

### 1. Install Dependencies
```bash
# Navigate to frontend directory
cd leaf-disease-detection/frontend

# Install npm packages
npm install
```

### 2. Configure Environment
The `.env` file is already configured with default backend URLs:
```
VITE_API_URL=http://localhost:8000
VITE_PREDICT_ENDPOINT=http://localhost:8000/api/predict
```

### 3. Run Development Server
```bash
npm run dev
```

The frontend will run on `http://localhost:5173`

### 4. Build for Production
```bash
npm run build
```

## Mock Data

The backend includes comprehensive mock data for all 38 plant disease classes. Each disease has:
- **Disease Name**: Common name of the disease
- **Severity Level**: Low, Moderate, High, or Critical
- **Confidence Score**: Prediction accuracy percentage
- **Description**: Detailed disease information
- **Causes**: What causes the disease
- **Symptoms**: Visual and structural symptoms
- **Treatment**: Recommended treatment procedures
- **Prevention**: Prevention strategies
- **Timeline**: Expected recovery time
- **Impact**: Potential crop impact

### Supported Classes (38 Total)
1. Apple___Apple_scab
2. Apple___Black_rot
3. Apple___Cedar_apple_rust
4. Apple___healthy
5. Blueberry___healthy
6. Cherry_(including_sour)___Powdery_mildew
7. Cherry_(including_sour)___healthy
8. Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot
9. Corn_(maize)___Common_rust_
10. Corn_(maize)___Northern_Leaf_Blight
11. Corn_(maize)___healthy
12. Grape___Black_rot
13. Grape___Esca_(Black_Measles)
14. Grape___Leaf_blight_(Isariopsis_Leaf_Spot)
15. Grape___healthy
16. Orange___Haunglongbing_(Citrus_greening)
17. Peach___Bacterial_spot
18. Peach___healthy
19. Pepper,_bell___Bacterial_spot
20. Pepper,_bell___healthy
21. Potato___Early_blight
22. Potato___Late_blight
23. Potato___healthy
24. Raspberry___healthy
25. Soybean___healthy
26. Squash___Powdery_mildew
27. Strawberry___Leaf_scorch
28. Strawberry___healthy
29. Tomato___Bacterial_spot
30. Tomato___Early_blight
31. Tomato___Late_blight
32. Tomato___Leaf_Mold
33. Tomato___Septoria_leaf_spot
34. Tomato___Spider_mites Two-spotted_spider_mite
35. Tomato___Target_Spot
36. Tomato___Tomato_Yellow_Leaf_Curl_Virus
37. Tomato___Tomato_mosaic_virus
38. Tomato___healthy

## API Endpoints

### Health Check
- **GET** `/health` - Server health status

### Classes
- **GET** `/api/classes` - Get all available disease classes

### Prediction
- **POST** `/api/predict` - Upload image and get prediction
  - Form Data: `file` (image file)
  - Response: Disease prediction with suggestions

### Suggestions
- **GET** `/api/suggestions/{disease_name}` - Get suggestions for specific disease
- **GET** `/api/all-suggestions` - Get all disease suggestions

### About
- **GET** `/api/about` - Get system information

## Features

### HomePage
- Hero section with call-to-action buttons
- Feature highlights
- Step-by-step workflow explanation
- Call-to-action section

### Prediction Page
- Drag-and-drop image upload interface
- Image preview functionality
- Real-time disease prediction
- Detailed disease information including:
  - Disease name and severity
  - Confidence percentage with visual progress bar
  - Detailed description
  - Causes and symptoms
  - Treatment recommendations
  - Prevention strategies
  - Recovery timeline
  - Potential impact

### About Page
- Project information
- Technology stack
- Supported plant diseases
- System architecture diagram
- Feature highlights
- Workflow explanation
- Benefits of the system

## Color Palette
- Primary: `#2E7D32` (Dark Green)
- Secondary: `#4CAF50` (Light Green)
- Background: `#F5FFF5` (Very Light Green)
- Text: `#1B1B1B` (Dark Gray)
- Success: `#2E7D32` (Green)
- Warning: `#FF9800` (Orange)
- Error: `#D32F2F` (Red)

## Adding Your Own Model

To use a trained model:

1. Place your `.h5` model file in `backend/model/plant_disease_model.h5`
2. Update `main.py` to load and use your model:
   ```python
   from tensorflow.keras.models import load_model
   model = load_model('model/plant_disease_model.h5')
   ```
3. Replace the mock prediction logic in the `/api/predict` endpoint

## Troubleshooting

### Backend Connection Issues
- Ensure backend is running on port 8000
- Check CORS settings in `main.py`
- Verify firewall settings

### File Upload Issues
- Ensure image format is PNG, JPG, or JPEG
- Check file size limits
- Verify permissions

### Frontend Not Loading
- Clear browser cache
- Restart development server
- Check console for errors

## Development Tips

1. **Backend Development**
   - Use FastAPI automatic API documentation at `/docs`
   - Enable debug mode for better error messages
   - Use Postman or Insomnia for API testing

2. **Frontend Development**
   - Use browser DevTools for React debugging
   - Enable React Developer Tools extension
   - Use Vite's HMR for fast refresh

3. **Mock Data Testing**
   - The system randomly selects a disease class for testing
   - Each class has detailed mock data with 5+ lines per field
   - Perfect for testing UI without a trained model

## Next Steps

1. Train a TensorFlow model on plant disease datasets
2. Replace mock predictions with actual model inference
3. Deploy to production (Heroku, AWS, Docker, etc.)
4. Add user authentication
5. Implement database for storing predictions
6. Add image history/gallery feature
7. Implement multi-language support

## Support

For issues or questions:
1. Check the API documentation at `http://localhost:8000/docs`
2. Review error messages in browser console and backend logs
3. Ensure all dependencies are correctly installed

## License
MIT License - Feel free to use this project for learning and development.

---

**Happy detecting! 🌿**
