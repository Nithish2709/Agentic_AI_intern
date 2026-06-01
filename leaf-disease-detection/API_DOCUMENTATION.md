# API Documentation

## Base URL
```
http://localhost:8000
```

## Authentication
Currently, no authentication is required. Future versions will include JWT-based authentication.

---

## Endpoints

### 1. Root Endpoint

**GET** `/`

Get basic API information.

**Response:**
```json
{
  "message": "Leaf Disease Detection System API",
  "version": "1.0.0",
  "status": "Running"
}
```

---

### 2. Health Check

**GET** `/health`

Check if the API server is running and healthy.

**Response:**
```json
{
  "status": "healthy",
  "service": "Leaf Disease Detection API",
  "version": "1.0.0"
}
```

---

### 3. Get All Classes

**GET** `/api/classes`

Retrieve all available disease classes.

**Response:**
```json
{
  "total_classes": 38,
  "classes": {
    "0": "Apple___Apple_scab",
    "1": "Apple___Black_rot",
    "2": "Apple___Cedar_apple_rust",
    ...
    "37": "Tomato___healthy"
  }
}
```

---

### 4. Predict Disease

**POST** `/api/predict`

Upload a leaf image and get disease prediction.

**Parameters:**
- `file` (FormData, required) - Leaf image file (PNG, JPG, JPEG, etc.)

**Request Example:**
```bash
curl -X POST \
  -F "file=@path/to/leaf_image.jpg" \
  http://localhost:8000/api/predict
```

**Response (Success):**
```json
{
  "success": true,
  "predicted_class_id": 30,
  "predicted_class": "Tomato___Late_blight",
  "confidence": 93.7,
  "disease": "Late Blight",
  "severity": "Critical",
  "severity_color": "#D32F2F",
  "description": "Late blight is a devastating fungal disease that rapidly destroys tomato foliage and fruit.",
  "causes": "Caused by Phytophthora infestans oomycete, spread by rain and high humidity in cool conditions.",
  "symptoms": "Water-soaked lesions on leaves with white mold on undersides, rapid collapse of foliage, fruit rot.",
  "treatment": "Apply fungicide immediately at first sign. Remove infected plant material. Improve air circulation.",
  "prevention": "Use resistant varieties. Avoid overhead watering. Remove infected volunteers and wild potatoes.",
  "timeline": "1-2 weeks with intensive fungicide application",
  "impact": "Severe fruit loss; can cause complete crop failure"
}
```

**Response (Error):**
```json
{
  "success": false,
  "error": "Invalid file format",
  "message": "Error processing image"
}
```

---

### 5. Get Disease Suggestions

**GET** `/api/suggestions/{disease_name}`

Get detailed suggestions for a specific disease.

**Parameters:**
- `disease_name` (URL parameter, required) - Disease class name (e.g., "Tomato___Late_blight")

**Request Example:**
```bash
curl http://localhost:8000/api/suggestions/Tomato___Late_blight
```

**Response (Success):**
```json
{
  "success": true,
  "disease_name": "Tomato___Late_blight",
  "data": {
    "disease": "Late Blight",
    "severity": "Critical",
    "confidence": 93.7,
    "description": "...",
    "causes": "...",
    "symptoms": "...",
    "treatment": "...",
    "prevention": "...",
    "timeline": "...",
    "impact": "..."
  }
}
```

**Response (Not Found):**
```json
{
  "success": false,
  "error": "Disease not found",
  "message": "No suggestions found for Invalid_Disease_Name"
}
```

---

### 6. Get All Suggestions

**GET** `/api/all-suggestions`

Retrieve all disease suggestions at once.

**Response:**
```json
{
  "total_suggestions": 38,
  "suggestions": {
    "Apple___Apple_scab": {
      "disease": "Apple Scab",
      "severity": "High",
      "confidence": 92.5,
      ...
    },
    "Apple___Black_rot": {
      "disease": "Black Rot",
      "severity": "Critical",
      "confidence": 88.3,
      ...
    },
    ...
  }
}
```

---

### 7. Get System Information

**GET** `/api/about`

Get detailed information about the system.

**Response:**
```json
{
  "name": "Leaf Disease Detection System",
  "version": "1.0.0",
  "description": "AI-powered system for detecting plant diseases from leaf images",
  "technologies": ["FastAPI", "TensorFlow", "Keras", "React", "Python"],
  "supported_classes": 38,
  "author": "Agriculture AI Team"
}
```

---

## Data Models

### Disease Suggestion Object
```json
{
  "disease": "string",              // Disease name
  "severity": "string",             // Low | Moderate | High | Critical | None
  "confidence": "number",           // 0-100 (percentage)
  "description": "string",          // Detailed description
  "causes": "string",               // What causes the disease
  "symptoms": "string",             // Observable symptoms
  "treatment": "string",            // Recommended treatment
  "prevention": "string",           // Prevention methods
  "timeline": "string",             // Recovery timeline
  "impact": "string"                // Potential impact
}
```

### Prediction Response Object
```json
{
  "success": "boolean",
  "predicted_class_id": "integer",
  "predicted_class": "string",
  "confidence": "number",
  "disease": "string",
  "severity": "string",
  "severity_color": "string",       // Hex color code
  "description": "string",
  "causes": "string",
  "symptoms": "string",
  "treatment": "string",
  "prevention": "string",
  "timeline": "string",
  "impact": "string"
}
```

---

## Error Handling

### Common Error Responses

**400 Bad Request**
```json
{
  "detail": "Invalid request format"
}
```

**404 Not Found**
```json
{
  "success": false,
  "error": "Resource not found",
  "message": "The requested resource does not exist"
}
```

**422 Unprocessable Entity**
```json
{
  "detail": [
    {
      "loc": ["body", "file"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

**500 Internal Server Error**
```json
{
  "success": false,
  "error": "Internal server error",
  "message": "An unexpected error occurred"
}
```

---

## Status Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request |
| 404 | Not Found |
| 422 | Unprocessable Entity |
| 500 | Internal Server Error |

---

## Rate Limiting

Currently, no rate limiting is implemented. This may be added in future versions.

---

## CORS Configuration

The API is configured to accept requests from:
- `http://localhost:3000`
- `http://localhost:5173`
- `http://localhost:8000`

To add additional origins, modify the `CORSMiddleware` in `main.py`.

---

## Testing with cURL

### Test Health Check
```bash
curl http://localhost:8000/health
```

### Test Get Classes
```bash
curl http://localhost:8000/api/classes
```

### Test Get Suggestions
```bash
curl http://localhost:8000/api/suggestions/Tomato___Late_blight
```

### Test Prediction
```bash
curl -X POST \
  -F "file=@leaf_image.jpg" \
  http://localhost:8000/api/predict
```

### Test About Endpoint
```bash
curl http://localhost:8000/api/about
```

---

## Testing with Python

```python
import requests

# Test API
BASE_URL = "http://localhost:8000"

# Health check
response = requests.get(f"{BASE_URL}/health")
print(response.json())

# Get classes
response = requests.get(f"{BASE_URL}/api/classes")
print(response.json())

# Get suggestions
response = requests.get(f"{BASE_URL}/api/suggestions/Tomato___Late_blight")
print(response.json())

# Predict
with open("leaf_image.jpg", "rb") as img:
    files = {"file": img}
    response = requests.post(f"{BASE_URL}/api/predict", files=files)
    print(response.json())
```

---

## Testing with Postman

1. Open Postman
2. Create a new request
3. Set method to GET or POST as needed
4. Enter the endpoint URL
5. For POST requests, use Form-data and add "file" with your image
6. Click Send

---

## Interactive API Documentation

FastAPI provides automatic interactive API documentation at:

```
http://localhost:8000/docs          # Swagger UI
http://localhost:8000/redoc         # ReDoc
```

Use these interfaces to test all endpoints directly from your browser.

---

## Webhooks (Future)

Webhook support will be added in future versions for real-time notifications.

---

## Versioning

Current API version: **1.0.0**

Future versions may have breaking changes. The version is indicated in the response headers and documentation.

---

## Support & Feedback

For API support or feedback:
1. Check the interactive docs at `/docs`
2. Review error messages and status codes
3. Check the logs in the console
4. Report issues with detailed error messages

---

**Last Updated:** May 2024
**Maintained By:** Agriculture AI Team
