import { useState, useRef } from 'react';
import axios from 'axios';
import './PredictionPage.css';

const SEVERITY_META = {
  None:     { color: '#2E7D32', bg: '#e8f5e9', label: '✅ Healthy',         icon: '🌿' },
  Low:      { color: '#388e3c', bg: '#f1f8e9', label: '🟢 Low Risk',        icon: '🍃' },
  Moderate: { color: '#f57c00', bg: '#fff3e0', label: '🟡 Moderate Risk',   icon: '⚠️' },
  High:     { color: '#e65100', bg: '#fbe9e7', label: '🟠 High Risk',       icon: '🔥' },
  Critical: { color: '#c62828', bg: '#ffebee', label: '🔴 Critical',        icon: '🚨' },
};

function SkeletonLoader() {
  return (
    <div className="skeleton-wrap">
      <div className="skeleton skeleton-title" />
      <div className="skeleton skeleton-line" />
      <div className="skeleton skeleton-line short" />
      <div className="skeleton skeleton-bar" />
      <div className="skeleton skeleton-block" />
      <div className="skeleton skeleton-block" />
    </div>
  );
}

function PredictionPage() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [dragOver, setDragOver] = useState(false);
  const fileInputRef = useRef(null);

  const loadFile = (file) => {
    if (!file || !file.type.startsWith('image/')) return;
    setSelectedFile(file);
    setPrediction(null);
    setError(null);
    const reader = new FileReader();
    reader.onloadend = () => setPreview(reader.result);
    reader.readAsDataURL(file);
  };

  const handlePredict = async () => {
    if (!selectedFile) { setError('Please select an image first'); return; }
    setLoading(true);
    setError(null);
    setPrediction(null);
    try {
      const formData = new FormData();
      formData.append('file', selectedFile);
      const res = await axios.post(import.meta.env.VITE_PREDICT_ENDPOINT, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      if (res.data.success) setPrediction(res.data);
      else setError(res.data.error || 'Prediction failed');
    } catch {
      setError('Cannot connect to server. Make sure the backend is running.');
    } finally {
      setLoading(false);
    }
  };

  const reset = () => { setSelectedFile(null); setPreview(null); setPrediction(null); setError(null); };

  const meta = prediction ? (SEVERITY_META[prediction.severity] || SEVERITY_META.None) : null;

  return (
    <div className="prediction-page">
      <div className="prediction-container">

        {/* ── Left: Upload ── */}
        <div className="upload-section">
          <div className="upload-card">
            <h2 className="card-title">🌿 Upload Leaf Image</h2>
            {/* single hidden input, triggered by ref */}
            <input
              ref={fileInputRef}
              type="file"
              accept="image/*"
              style={{ display: 'none' }}
              onChange={(e) => loadFile(e.target.files[0])}
            />

            <div
              className={`drag-drop-area ${dragOver ? 'drag-active' : ''} ${preview ? 'has-preview' : ''}`}
              onClick={() => !preview && fileInputRef.current.click()}
              onDragOver={(e) => { e.preventDefault(); setDragOver(true); }}
              onDragLeave={() => setDragOver(false)}
              onDrop={(e) => { e.preventDefault(); setDragOver(false); loadFile(e.dataTransfer.files[0]); }}
            >
              {!preview ? (
                <div className="drag-drop-content">
                  <div className="upload-icon-wrap">
                    <span className="upload-icon">📤</span>
                  </div>
                  <p className="drag-title">Drag & drop your leaf image</p>
                  <p className="or-text">— or —</p>
                  <button
                    type="button"
                    className="file-input-label"
                    onClick={(e) => { e.stopPropagation(); fileInputRef.current.click(); }}
                  >
                    Browse Files
                  </button>
                  <p className="file-hint">PNG, JPG, JPEG supported</p>
                </div>
              ) : (
                <div className="preview-content">
                  <img src={preview} alt="Leaf preview" className="preview-image" />
                  <div className="preview-meta">
                    <span className="preview-filename">📎 {selectedFile.name}</span>
                    <button
                      type="button"
                      className="change-file-label"
                      onClick={(e) => { e.stopPropagation(); fileInputRef.current.click(); }}
                    >
                      Change
                    </button>
                  </div>
                </div>
              )}
            </div>
          </div>

          <button
            className={`btn btn-primary predict-btn ${loading ? 'loading' : ''}`}
            onClick={handlePredict}
            disabled={loading || !selectedFile}
          >
            {loading ? (
              <><span className="spinner" /> Analyzing...</>
            ) : (
              '🔬 Predict Disease'
            )}
          </button>

          {error && <div className="error-message">⚠️ {error}</div>}
        </div>

        {/* ── Right: Results ── */}
        <div className="results-section">
          {!prediction && !loading && (
            <div className="no-results">
              <div className="no-results-icon">🔍</div>
              <p className="no-results-title">No Analysis Yet</p>
              <p>Upload a leaf image and click <strong>Predict Disease</strong> to see results here.</p>
            </div>
          )}

          {loading && <SkeletonLoader />}

          {prediction && !loading && (
            <div className="results-card">

              {/* Header */}
              <div className="result-header" style={{ borderColor: meta.color + '40' }}>
                <div>
                  <p className="result-label">Detected Disease</p>
                  <h2 className="disease-name">{prediction.disease}</h2>
                  <p className="predicted-class">{prediction.predicted_class.replace(/___/g, ' › ').replace(/_/g, ' ')}</p>
                </div>
                <div className="severity-badge" style={{ background: meta.bg, color: meta.color, borderColor: meta.color + '40' }}>
                  {meta.label}
                </div>
              </div>

              {/* Confidence */}
              <div className="confidence-section">
                <div className="confidence-header">
                  <span className="info-label">Confidence</span>
                  <span className="confidence-value" style={{ color: meta.color }}>{prediction.confidence}%</span>
                </div>
                <div className="confidence-track">
                  <div
                    className="confidence-fill"
                    style={{ width: `${prediction.confidence}%`, background: `linear-gradient(90deg, ${meta.color}99, ${meta.color})` }}
                  />
                </div>
              </div>

              {/* Top 3 */}
              {prediction.top3_predictions && (
                <div className="top3-section">
                  <p className="info-label">Top Predictions</p>
                  <div className="top3-list">
                    {prediction.top3_predictions.map((p, i) => (
                      <div className="top3-item" key={i}>
                        <span className="top3-rank">#{i + 1}</span>
                        <span className="top3-name">{p.class.replace(/___/g, ' › ').replace(/_/g, ' ')}</span>
                        <span className="top3-conf">{p.confidence}%</span>
                        <div className="top3-bar-track">
                          <div className="top3-bar-fill" style={{ width: `${p.confidence}%`, animationDelay: `${i * 0.1}s` }} />
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Info Grid */}
              <div className="info-grid">
                {[
                  { label: '📋 Description', value: prediction.description },
                  { label: '🦠 Causes', value: prediction.causes },
                  { label: '🔎 Symptoms', value: prediction.symptoms },
                ].map(({ label, value }) => (
                  <div className="info-item" key={label}>
                    <span className="info-label">{label}</span>
                    <p>{value}</p>
                  </div>
                ))}
              </div>

              {/* Treatment Cards */}
              <div className="treatment-grid">
                {[
                  { icon: '💊', title: 'Treatment', value: prediction.treatment },
                  { icon: '🛡️', title: 'Prevention', value: prediction.prevention },
                  { icon: '⏱️', title: 'Recovery Timeline', value: prediction.timeline },
                  { icon: '📉', title: 'Impact', value: prediction.impact },
                ].map(({ icon, title, value }) => (
                  <div className="treatment-card" key={title}>
                    <div className="treatment-card-header">
                      <span>{icon}</span>
                      <strong>{title}</strong>
                    </div>
                    <p>{value}</p>
                  </div>
                ))}
              </div>

              <button className="btn btn-secondary reset-btn" onClick={reset}>
                ↩ Analyze Another Image
              </button>
            </div>
          )}
        </div>

      </div>
    </div>
  );
}

export default PredictionPage;
