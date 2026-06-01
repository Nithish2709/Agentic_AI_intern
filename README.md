# Leaf Disease Detection System

A full-stack application for detecting plant diseases from leaf images using a React frontend and a FastAPI backend.

## Repository Layout

This repository contains the Leaf Disease Detection project under the `leaf-disease-detection/` folder.

```text
leaf-disease-detection/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── model/
│       └── best_model.h5
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   ├── vite.config.js
│   └── .env
├── API_DOCUMENTATION.md
├── MOCK_DATA_REFERENCE.md
├── PROJECT_DELIVERY_SUMMARY.md
├── PROJECT_README.md
├── SETUP_GUIDE.md
└── TESTING_GUIDE.md
`

## What it does

- Uploads a leaf image (.png, .jpg, etc.)
- Sends the image to the backend
- Uses a trained Keras model to detect plant disease
- Returns disease name, confidence, severity, and care recommendations
- Displays results in a React-based UI

## Key Features

- Supports 38 plant disease classes
- FastAPI backend with image upload and prediction
- React + Vite frontend with drag-and-drop upload
- Detailed disease suggestions and prevention tips
- Mock data for disease descriptions and recommendations

## Tech Stack

- Frontend: React, Vite, Axios
- Backend: FastAPI, Uvicorn, TensorFlow, Keras
- Image processing: Pillow
- Environment management: python-dotenv

## Quick Start

### Backend

`powershell
cd leaf-disease-detection/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
`

The backend starts on http://localhost:8000.

### Frontend

`powershell
cd leaf-disease-detection/frontend
npm install
npm run dev
`

The frontend starts on http://localhost:5173.

## API Endpoints

- GET /health — health check
- GET /api/classes — list available disease classes
- POST /api/predict — submit a leaf image and get prediction
- GET /api/suggestions/{disease_name} — get treatment suggestions
- GET /api/all-suggestions — retrieve all suggestions
- GET /api/about — application metadata

## Notes

- The backend expects the model file at leaf-disease-detection/backend/model/best_model.h5.
- If the model file is not present, add it to the ackend/model/ folder before running the backend.
- Environment values for the frontend are stored in leaf-disease-detection/frontend/.env.

## Helpful Docs

- leaf-disease-detection/SETUP_GUIDE.md — full setup instructions
- leaf-disease-detection/API_DOCUMENTATION.md — API details
- leaf-disease-detection/MOCK_DATA_REFERENCE.md — disease mock data reference
- leaf-disease-detection/TESTING_GUIDE.md — test guidance
