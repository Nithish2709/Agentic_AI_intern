# 🌿 Leaf Disease Detection System

An advanced AI-powered web application that detects plant diseases from leaf images using deep learning. Simply upload a leaf image and get instant disease identification with detailed treatment recommendations.

![React](https://img.shields.io/badge/React-18.2-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.14-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## Features ✨

### 🔍 Accurate Disease Detection
- Identifies 38+ plant diseases
- High accuracy predictions using trained deep learning models
- Confidence scores for each prediction

### 📱 User-Friendly Interface
- Clean, intuitive React frontend
- Drag-and-drop image upload
- Real-time prediction results
- Responsive design for all devices

### 💡 Actionable Insights
- Detailed disease descriptions
- Causes and symptoms information
- Treatment recommendations
- Prevention strategies
- Expected recovery timeline
- Potential crop impact assessment

### ⚡ Fast Processing
- Instant predictions in seconds
- Optimized image processing
- Efficient API endpoints

### 🛠️ Complete Documentation
- Mock data for all disease classes
- Each class contains 5+ lines of detailed information
- Comprehensive setup guide
- API documentation

## Technology Stack 🛠️

### Frontend
- **React 18.2** - UI library
- **Vite** - Build tool & dev server
- **Axios** - HTTP client
- **CSS3** - Styling with custom properties

### Backend
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **TensorFlow/Keras** - Deep learning framework
- **Pillow** - Image processing

### AI/ML
- **TensorFlow** - Deep learning library
- **Keras** - Neural network API
- **NumPy** - Numerical computing

## Project Structure 📁

```
leaf-disease-detection/
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── HomePage.jsx          # Home page component
│   │   │   ├── HomePage.css
│   │   │   ├── PredictionPage.jsx    # Main prediction page
│   │   │   ├── PredictionPage.css
│   │   │   ├── AboutPage.jsx         # About page
│   │   │   └── AboutPage.css
│   │   ├── App.jsx                   # Main app component
│   │   ├── App.css
│   │   ├── main.jsx                  # Entry point
│   │   └── index.css                 # Global styles
│   ├── public/                       # Static files
│   ├── index.html                    # HTML template
│   ├── vite.config.js                # Vite configuration
│   ├── package.json                  # NPM dependencies
│   └── .env                          # Environment variables
├── backend/
│   ├── main.py                       # FastAPI application with mock data
│   ├── requirements.txt              # Python dependencies
│   └── model/
│       └── plant_disease_model.h5    # Trained model (to be added)
├── SETUP_GUIDE.md                    # Detailed setup instructions
└── README.md                         # This file
```

## Quick Start 🚀

### Prerequisites
- Python 3.8+ 
- Node.js 16+
- npm or yarn

### Backend Setup

```bash
# Navigate to backend
cd leaf-disease-detection/backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
python main.py
```

Backend runs on `http://localhost:8000`

### Frontend Setup

```bash
# Navigate to frontend
cd leaf-disease-detection/frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend runs on `http://localhost:5173`

## API Endpoints 📡

### Health & Info
```
GET  /                    # Root endpoint
GET  /health             # Health check
GET  /api/about          # System info
```

### Classes & Predictions
```
GET  /api/classes                      # Get all disease classes
POST /api/predict                      # Upload image and get prediction
GET  /api/suggestions/{disease_name}   # Get disease suggestions
GET  /api/all-suggestions             # Get all suggestions
```

### Example Prediction Request
```bash
curl -X POST \
  -F "file=@leaf_image.jpg" \
  http://localhost:8000/api/predict
```

### Example Response
```json
{
  "success": true,
  "predicted_class_id": 30,
  "predicted_class": "Tomato___Late_blight",
  "confidence": 93.7,
  "disease": "Late Blight",
  "severity": "Critical",
  "description": "Late blight is a devastating fungal disease...",
  "causes": "Caused by Phytophthora infestans oomycete...",
  "symptoms": "Water-soaked lesions on leaves with white mold...",
  "treatment": "Apply fungicide immediately at first sign...",
  "prevention": "Use resistant varieties. Avoid overhead watering...",
  "timeline": "1-2 weeks with intensive fungicide program",
  "impact": "Severe fruit loss; can cause complete crop failure"
}
```

## Supported Plant Diseases 🌱

The system can identify **38 different plant diseases** across:

- **Apple**: Apple scab, Black rot, Cedar apple rust
- **Blueberry**: Healthy status monitoring
- **Cherry**: Powdery mildew detection
- **Corn**: Cercospora leaf spot, Common rust, Northern Leaf Blight
- **Grape**: Black rot, Esca, Leaf blight
- **Orange**: Haunglongbing (Citrus greening)
- **Peach**: Bacterial spot detection
- **Pepper**: Bacterial spot detection
- **Potato**: Early blight, Late blight
- **Raspberry**: Healthy status monitoring
- **Soybean**: Healthy status monitoring
- **Squash**: Powdery mildew detection
- **Strawberry**: Leaf scorch detection
- **Tomato**: Bacterial spot, Early blight, Late blight, Leaf Mold, Septoria leaf spot, Spider mites, Target Spot, TYLCV, Mosaic virus

## Mock Data Features 📊

Each disease class includes comprehensive mock data with 5+ detailed information fields:

1. **Disease Name** - Common and scientific name
2. **Severity Level** - None, Low, Moderate, High, or Critical
3. **Confidence Score** - Accuracy percentage (85-98%)
4. **Description** - Detailed disease overview
5. **Causes** - What causes the disease
6. **Symptoms** - Observable symptoms
7. **Treatment** - Recommended treatment procedures
8. **Prevention** - Prevention strategies
9. **Timeline** - Expected recovery time
10. **Impact** - Potential agricultural impact

## Pages Overview 📄

### Home Page
- Hero section with call-to-action
- Feature highlights
- Step-by-step workflow
- Technology benefits

### Prediction Page
- Drag-and-drop upload interface
- Image preview
- Real-time analysis
- Comprehensive results display
- Confidence visualization

### About Page
- Project information
- Technology stack details
- Supported disease list
- System architecture diagram
- Workflow explanation
- Feature highlights

## Color Scheme 🎨

```
Primary Green:    #2E7D32
Secondary Green:  #4CAF50
Background:       #F5FFF5
Text:             #1B1B1B
Warning:          #FF9800
Error:            #D32F2F
Success:          #2E7D32
```

## Development Guide 👨‍💻

### Adding a Real Model

1. Train your model on plant disease dataset
2. Export as `.h5` file
3. Place in `backend/model/plant_disease_model.h5`
4. Update prediction logic in `main.py`:

```python
from tensorflow.keras.models import load_model

model = load_model('model/plant_disease_model.h5')

# In predict endpoint:
predicted_class_id = np.argmax(model.predict(processed_image))
```

### Customizing Mock Data

Edit `DISEASE_SUGGESTIONS` dictionary in `backend/main.py` to add or modify disease information.

### Extending Features

1. Add user authentication
2. Implement database for prediction history
3. Add image gallery
4. Multi-language support
5. Mobile app version

## Performance Optimization ⚙️

- **Frontend**: Lazy loading, code splitting, image optimization
- **Backend**: Model caching, async processing, request batching
- **Database**: Query optimization, indexing (when added)

## Error Handling 🔧

The system handles:
- Invalid image formats
- Large file uploads
- Server connection issues
- Model prediction errors
- CORS requests

## Browser Support 🌐

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Opera 76+

## Deployment Options 🚀

### Frontend
- Vercel
- Netlify
- GitHub Pages
- AWS S3 + CloudFront

### Backend
- Heroku
- AWS EC2
- Google Cloud Run
- Docker containers

### Docker Deployment
```bash
# Build frontend
cd frontend && npm run build

# Build and run backend with Docker
docker build -t leaf-detection-backend .
docker run -p 8000:8000 leaf-detection-backend
```

## Troubleshooting 🐛

| Issue | Solution |
|-------|----------|
| Backend not responding | Check if running on port 8000, restart service |
| Image upload fails | Verify file format (PNG/JPG), check file size |
| CORS errors | Ensure backend is running, check CORS settings |
| Frontend not loading | Clear cache, restart dev server, check console |
| Predictions timeout | Check image size, verify backend performance |

## Contributing 🤝

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Future Enhancements 🔮

- [ ] User authentication system
- [ ] Prediction history database
- [ ] Multi-language support
- [ ] Mobile app version
- [ ] Real-time disease tracking
- [ ] Farmer community features
- [ ] Weather integration
- [ ] Crop management recommendations

## FAQ ❓

**Q: Can I use this for commercial purposes?**
A: Yes, under the MIT license with attribution.

**Q: How accurate is the system?**
A: Mock data shows 85-98% confidence. Actual accuracy depends on trained model quality.

**Q: What image formats are supported?**
A: PNG, JPG, JPEG, and other common image formats.

**Q: Can I add my own disease classes?**
A: Yes, add new entries to `CLASS_LABELS` and `DISEASE_SUGGESTIONS` in backend.

**Q: Is internet required?**
A: Backend needs to be running locally or on a server.

## License 📄

MIT License - See LICENSE file for details

## Acknowledgments 🙏

- Built with React, FastAPI, and TensorFlow
- Inspired by agricultural AI research
- UI design follows modern web standards

## Support 📞

For issues and questions:
1. Check [SETUP_GUIDE.md](SETUP_GUIDE.md)
2. Review API documentation at `/docs`
3. Check browser console for errors
4. Verify backend logs

---

**Made with 🌱 for agriculture and farmers**

[View Setup Guide](SETUP_GUIDE.md) • [API Docs](http://localhost:8000/docs) • [Report Issues](https://github.com/)

