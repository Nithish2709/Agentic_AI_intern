import { useState, useEffect } from 'react';
import axios from 'axios';
import './AboutPage.css';

function AboutPage() {
  const [aboutData, setAboutData] = useState(null);
  const [classes, setClasses] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([
      axios.get(import.meta.env.VITE_API_URL + '/api/about'),
      axios.get(import.meta.env.VITE_CLASSES_ENDPOINT),
    ]).then(([a, c]) => {
      setAboutData(a.data);
      setClasses(c.data);
    }).catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return (
    <div className="about-page">
      <div className="about-skeleton">
        {[1,2,3].map(i => <div key={i} className="skeleton-section" />)}
      </div>
    </div>
  );

  const archSteps = ['User', 'React Frontend', 'FastAPI Backend', 'TensorFlow Model', 'Prediction', 'Suggestion'];

  return (
    <div className="about-page">

      {/* Header */}
      <section className="about-header">
        <div className="about-header-content">
          <div className="about-badge">🌿 Open Source · AI-Powered</div>
          <h1>Leaf Disease Detection System</h1>
          <p>Advanced deep learning technology to protect crops and improve agricultural outcomes.</p>
        </div>
      </section>

      {/* Info Cards */}
      {aboutData && (
        <section className="about-section">
          <h2 className="section-title">Project Overview</h2>
          <div className="info-cards">
            {[
              { label: 'System Name', value: aboutData.name, icon: '🌿' },
              { label: 'Version', value: aboutData.version, icon: '🏷️' },
              { label: 'Disease Classes', value: `${aboutData.supported_classes} Classes`, icon: '🔬' },
            ].map(({ label, value, icon }) => (
              <div className="info-card" key={label}>
                <span className="info-card-icon">{icon}</span>
                <div>
                  <p className="info-card-label">{label}</p>
                  <p className="info-card-value">{value}</p>
                </div>
              </div>
            ))}
          </div>
          <p className="about-description">{aboutData.description}</p>
        </section>
      )}

      {/* Technologies */}
      {aboutData?.technologies && (
        <section className="about-section">
          <h2 className="section-title">Technologies Used</h2>
          <div className="tech-grid">
            {[
              { name: 'React', icon: '⚛️', desc: 'Frontend UI' },
              { name: 'FastAPI', icon: '⚡', desc: 'Backend API' },
              { name: 'TensorFlow', icon: '🧠', desc: 'ML Framework' },
              { name: 'Keras (.h5)', icon: '📦', desc: 'Model Format' },
              { name: 'Python', icon: '🐍', desc: 'Backend Language' },
            ].map(({ name, icon, desc }) => (
              <div className="tech-card" key={name}>
                <span className="tech-icon">{icon}</span>
                <strong>{name}</strong>
                <span>{desc}</span>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Architecture */}
      <section className="about-section">
        <h2 className="section-title">System Architecture</h2>
        <div className="architecture">
          {archSteps.map((step, i) => (
            <div key={step} className="arch-row" style={{ animationDelay: `${i * 0.08}s` }}>
              <div className="arch-node">{step}</div>
              {i < archSteps.length - 1 && <div className="arch-arrow">↓</div>}
            </div>
          ))}
        </div>
      </section>

      {/* Supported Classes */}
      {classes && (
        <section className="about-section">
          <h2 className="section-title">Supported Plant Diseases <span className="class-count">{classes.total_classes}</span></h2>
          <div className="classes-grid">
            {Object.values(classes.classes).map((name, i) => {
              const isHealthy = name.includes('healthy');
              return (
                <div
                  key={i}
                  className={`disease-chip ${isHealthy ? 'healthy' : 'diseased'}`}
                  style={{ animationDelay: `${Math.min(i * 0.02, 0.5)}s` }}
                >
                  {isHealthy ? '✅' : '🔴'} {name.replace(/___/g, ' › ').replace(/_/g, ' ')}
                </div>
              );
            })}
          </div>
        </section>
      )}

    </div>
  );
}

export default AboutPage;
