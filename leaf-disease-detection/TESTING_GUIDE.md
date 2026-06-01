# Testing Guide & Demo

This guide explains how to test the Leaf Disease Detection System with mock data.

## Quick Start Testing

### 1. Start the Backend
```bash
cd leaf-disease-detection/backend
python main.py
```

The backend will start on `http://localhost:8000`

### 2. Start the Frontend
In a new terminal:
```bash
cd leaf-disease-detection/frontend
npm run dev
```

The frontend will start on `http://localhost:5173`

### 3. Open in Browser
Navigate to `http://localhost:5173`

---

## API Testing

### Method 1: Browser-Based API Documentation

1. Go to `http://localhost:8000/docs`
2. You'll see the interactive Swagger UI
3. Click on any endpoint to expand it
4. Click "Try it out"
5. Fill in any required parameters
6. Click "Execute"

### Method 2: Using cURL

Test all endpoints from your terminal:

#### Test Health Check
```bash
curl http://localhost:8000/health
```

#### Test Get Classes
```bash
curl http://localhost:8000/api/classes
```

#### Test Get All Suggestions
```bash
curl http://localhost:8000/api/all-suggestions
```

#### Test Single Disease Suggestion
```bash
curl http://localhost:8000/api/suggestions/Tomato___Late_blight
```

#### Test About Endpoint
```bash
curl http://localhost:8000/api/about
```

#### Test Prediction (requires image)
```bash
curl -X POST \
  -F "file=@path/to/your/image.jpg" \
  http://localhost:8000/api/predict
```

### Method 3: Using Python Requests

Create a file `test_api.py`:

```python
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    print("=== Testing Health Check ===")
    response = requests.get(f"{BASE_URL}/health")
    print(json.dumps(response.json(), indent=2))
    print()

def test_classes():
    print("=== Testing Get Classes ===")
    response = requests.get(f"{BASE_URL}/api/classes")
    data = response.json()
    print(f"Total classes: {data['total_classes']}")
    print("First 5 classes:")
    for key in list(data['classes'].keys())[:5]:
        print(f"  {key}: {data['classes'][key]}")
    print()

def test_suggestions():
    print("=== Testing Disease Suggestions ===")
    diseases = ["Tomato___Late_blight", "Apple___Black_rot", "Potato___Early_blight"]
    for disease in diseases:
        response = requests.get(f"{BASE_URL}/api/suggestions/{disease}")
        data = response.json()
        if data['success']:
            suggestion = data['data']
            print(f"\n{disease}:")
            print(f"  Disease: {suggestion['disease']}")
            print(f"  Severity: {suggestion['severity']}")
            print(f"  Confidence: {suggestion['confidence']}%")
            print(f"  Description: {suggestion['description'][:80]}...")
            print(f"  Treatment: {suggestion['treatment'][:80]}...")
        else:
            print(f"  Error: {data['error']}")
    print()

def test_about():
    print("=== Testing About Endpoint ===")
    response = requests.get(f"{BASE_URL}/api/about")
    print(json.dumps(response.json(), indent=2))
    print()

def test_prediction():
    print("=== Testing Prediction ===")
    # Note: You need to have an actual image file
    image_path = "path/to/your/image.jpg"  # Replace with actual path
    try:
        with open(image_path, "rb") as img:
            files = {"file": img}
            response = requests.post(f"{BASE_URL}/api/predict", files=files)
            print(json.dumps(response.json(), indent=2))
    except FileNotFoundError:
        print(f"Image not found at {image_path}")
        print("Please provide an actual image file to test prediction")
    print()

if __name__ == "__main__":
    print("Starting API Tests...\n")
    test_health()
    test_about()
    test_classes()
    test_suggestions()
    test_prediction()
    print("Tests completed!")
```

Run it:
```bash
python test_api.py
```

---

## Frontend Testing

### Test Home Page
1. Navigate to `http://localhost:5173`
2. You should see:
   - Hero section with "Leaf Disease Detection System"
   - "Upload Image" and "Learn More" buttons
   - Features section with 4 cards
   - How It Works section with 4 steps
   - Call-to-action section

### Test Navigation
1. Click on "Predict" in the navigation
2. You should see the prediction page with:
   - Drag-and-drop upload area on the left
   - Results area on the right (empty initially)

3. Click on "About" in the navigation
4. You should see:
   - Project information
   - Technology stack
   - List of 38 supported diseases
   - System architecture diagram
   - Feature highlights

### Test Upload Functionality

#### Test Drag and Drop
1. Find any image file on your computer
2. Go to the Prediction page
3. Drag the image file onto the drag-drop area
4. The image should appear as a preview

#### Test File Chooser
1. Click the "Choose File" button
2. Select an image from your file system
3. The image should appear as a preview

#### Test Change Image
1. With an image uploaded, click "Change Image"
2. Select a different image
3. The preview should update

### Test Prediction
1. Upload an image (any image file)
2. Click "Predict Disease"
3. You should see loading state ("Analyzing...")
4. Wait a few seconds
5. Results should appear showing:
   - Disease name
   - Severity badge
   - Confidence progress bar
   - Full disease information
   - Treatment recommendations
   - Prevention strategies

### Test Responsive Design
1. Open developer tools (F12)
2. Toggle device toolbar
3. Test different screen sizes:
   - Mobile (375px)
   - Tablet (768px)
   - Desktop (1024px+)
4. Verify layout adjusts properly

---

## Mock Data Testing

### Verify Mock Data Structure

Each disease in the system has at least 5 detailed information fields:

```python
{
    'disease': str,        # 1+ lines
    'severity': str,       # 1 line
    'confidence': float,   # 1 line (85-98%)
    'description': str,    # 2+ lines
    'causes': str,         # 2+ lines
    'symptoms': str,       # 2+ lines
    'treatment': str,      # 3+ lines
    'prevention': str,     # 2+ lines
    'timeline': str,       # 1+ line
    'impact': str          # 1+ line
}
```

Total: **10 information fields per disease, 5+ lines minimum**

### Test Mock Data Script

Create `test_mock_data.py`:

```python
import requests
import json

BASE_URL = "http://localhost:8000"

def test_mock_data_completeness():
    """Verify all mock data has sufficient information"""
    response = requests.get(f"{BASE_URL}/api/all-suggestions")
    suggestions = response.json()['suggestions']
    
    required_fields = [
        'disease', 'severity', 'confidence', 'description',
        'causes', 'symptoms', 'treatment', 'prevention', 'timeline', 'impact'
    ]
    
    min_line_requirements = {
        'disease': 1,
        'severity': 1,
        'confidence': 1,
        'description': 2,
        'causes': 2,
        'symptoms': 2,
        'treatment': 3,
        'prevention': 2,
        'timeline': 1,
        'impact': 1
    }
    
    total_diseases = len(suggestions)
    complete_count = 0
    incomplete_diseases = []
    
    for disease_name, data in suggestions.items():
        # Check all fields exist
        missing_fields = [f for f in required_fields if f not in data]
        if missing_fields:
            incomplete_diseases.append({
                'disease': disease_name,
                'missing_fields': missing_fields
            })
            continue
        
        # Check line count for each field
        is_complete = True
        for field, min_lines in min_line_requirements.items():
            lines = len(data[field].strip().split('\n'))
            if lines < min_lines:
                incomplete_diseases.append({
                    'disease': disease_name,
                    'field': field,
                    'required_lines': min_lines,
                    'actual_lines': lines
                })
                is_complete = False
        
        if is_complete:
            complete_count += 1
    
    print(f"Total Diseases: {total_diseases}")
    print(f"Complete Data: {complete_count}")
    print(f"Incomplete: {len(incomplete_diseases)}")
    
    if incomplete_diseases:
        print("\nIncomplete Entries:")
        for entry in incomplete_diseases[:5]:
            print(f"  - {entry}")
    else:
        print("\n✅ All mock data is complete!")

if __name__ == "__main__":
    test_mock_data_completeness()
```

Run it:
```bash
python test_mock_data.py
```

---

## Stress Testing

### Test High Frequency Predictions
```python
import requests
import time
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "http://localhost:8000"

def make_prediction(image_path, index):
    try:
        with open(image_path, "rb") as img:
            start = time.time()
            response = requests.post(f"{BASE_URL}/api/predict", files={"file": img})
            elapsed = time.time() - start
            print(f"Request {index}: {response.status_code} - {elapsed:.2f}s")
            return elapsed
    except Exception as e:
        print(f"Request {index}: Error - {str(e)}")
        return None

# Test with 10 concurrent requests
image_path = "path/to/your/image.jpg"
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(make_prediction, image_path, i) for i in range(10)]
    times = [f.result() for f in futures]

avg_time = sum(t for t in times if t) / len([t for t in times if t])
print(f"\nAverage response time: {avg_time:.2f}s")
```

---

## Performance Testing

### Measure API Response Times
```python
import requests
import time

BASE_URL = "http://localhost:8000"

endpoints = [
    "/health",
    "/api/classes",
    "/api/all-suggestions",
    "/api/about",
    "/api/suggestions/Tomato___Late_blight"
]

print("Performance Test Results:\n")
for endpoint in endpoints:
    start = time.time()
    response = requests.get(f"{BASE_URL}{endpoint}")
    elapsed = time.time() - start
    print(f"{endpoint}")
    print(f"  Status: {response.status_code}")
    print(f"  Time: {elapsed*1000:.2f}ms")
    print()
```

---

## Troubleshooting Tests

### Backend Not Starting
- Check if port 8000 is available
- Verify Python version (3.8+)
- Install all requirements: `pip install -r requirements.txt`

### Frontend Not Loading
- Check if port 5173 is available
- Clear npm cache: `npm cache clean --force`
- Reinstall dependencies: `npm install`

### Prediction Errors
- Verify image format (PNG/JPG)
- Check file size (shouldn't be too large)
- Ensure backend is running

### CORS Errors
- Backend CORS is configured for `http://localhost:5173`
- Check browser console for specific errors

---

## Test Checklist

### Backend Tests ✅
- [ ] Health check works
- [ ] Get classes endpoint returns 38 classes
- [ ] Get all suggestions returns all diseases
- [ ] Get specific suggestion works
- [ ] Prediction endpoint accepts images
- [ ] About endpoint returns system info
- [ ] API docs available at `/docs`

### Frontend Tests ✅
- [ ] Home page loads correctly
- [ ] All navigation links work
- [ ] Prediction page loads
- [ ] Drag-and-drop upload works
- [ ] File chooser works
- [ ] Change image button works
- [ ] Prediction button triggers API call
- [ ] Results display correctly
- [ ] About page shows all 38 diseases
- [ ] Responsive design works

### Mock Data Tests ✅
- [ ] All 38 classes have suggestions
- [ ] Each suggestion has 10 fields
- [ ] Each field has minimum 5 lines total
- [ ] Disease information is realistic
- [ ] Confidence scores are realistic (85-98%)
- [ ] Severity levels are appropriate

---

## Continuous Testing

### Automated Test Script

Create `continuous_test.py`:

```python
import requests
import time
import json

BASE_URL = "http://localhost:8000"

def continuous_health_check(interval=5, duration=60):
    start_time = time.time()
    check_count = 0
    failed_checks = 0
    
    while time.time() - start_time < duration:
        try:
            response = requests.get(f"{BASE_URL}/health", timeout=5)
            if response.status_code == 200:
                check_count += 1
            else:
                failed_checks += 1
        except Exception as e:
            failed_checks += 1
        
        time.sleep(interval)
    
    print(f"Health Checks: {check_count}")
    print(f"Failed: {failed_checks}")
    print(f"Success Rate: {(check_count/(check_count+failed_checks)*100):.1f}%")

if __name__ == "__main__":
    print("Running continuous health checks for 60 seconds...")
    continuous_health_check()
```

---

## Expected Results

### Successful Prediction
```json
{
  "success": true,
  "predicted_class": "Tomato___Late_blight",
  "disease": "Late Blight",
  "severity": "Critical",
  "confidence": 93.7,
  "treatment": "Apply fungicide immediately..."
}
```

### Successful About Response
```json
{
  "name": "Leaf Disease Detection System",
  "supported_classes": 38,
  "technologies": ["FastAPI", "TensorFlow", "Keras", "React"]
}
```

---

## Report Issues

If you encounter any issues during testing:
1. Note the exact error message
2. Check the browser console (F12)
3. Check backend logs
4. Verify all dependencies are installed
5. Try restarting both services

---

**Happy Testing! 🌿**

For more information, see [API_DOCUMENTATION.md](API_DOCUMENTATION.md) and [SETUP_GUIDE.md](SETUP_GUIDE.md)
