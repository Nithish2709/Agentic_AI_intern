import './HomePage.css';

function HomePage({ onNavigate }) {
  return (
    <div className="home-page">

      {/* Hero */}
      <section className="hero">
        <div className="hero-bg-circles">
          <span /><span /><span />
        </div>
        <div className="hero-content">
          <div className="hero-badge">🤖 AI-Powered Detection</div>
          <h1>Detect Plant Diseases Instantly</h1>
          <p>Upload a leaf image and get accurate disease identification with treatment recommendations — powered by deep learning.</p>
          <div className="hero-buttons">
            <button className="btn btn-primary" onClick={() => onNavigate('predict')}>
              🔍 Analyze Leaf
            </button>
            <button className="btn btn-secondary" onClick={() => document.querySelector('.how-it-works').scrollIntoView({ behavior: 'smooth' })}>
              Learn More
            </button>
          </div>
          <div className="hero-stats">
            <div className="hero-stat">
              <strong>38</strong>
              <span>Disease Classes</span>
            </div>
            <div className="hero-stat">
              <strong>95%+</strong>
              <span>Accuracy</span>
            </div>
            <div className="hero-stat">
              <strong>&lt;2s</strong>
              <span>Prediction Time</span>
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="features">
        <div className="section-header">
          <h2>Why Use Our System?</h2>
          <p>Everything you need to protect your crops</p>
        </div>
        <div className="features-grid">
          {[
            { icon: '🔍', title: 'Disease Detection', desc: 'Accurate identification of 38 plant diseases using advanced deep learning models.' },
            { icon: '🧠', title: 'AI-Powered Analysis', desc: 'Trained on thousands of real leaf images for reliable, production-ready predictions.' },
            { icon: '💡', title: 'Treatment Suggestions', desc: 'Get detailed treatment, prevention, and recovery timeline for every detected disease.' },
            { icon: '⚡', title: 'Instant Results', desc: 'Get predictions with confidence scores in under 2 seconds.' },
          ].map(({ icon, title, desc }) => (
            <div className="feature-card" key={title}>
              <div className="feature-icon-wrap">{icon}</div>
              <h3>{title}</h3>
              <p>{desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* How It Works */}
      <section className="how-it-works">
        <div className="section-header">
          <h2>How It Works</h2>
          <p>Simple steps to identify and treat plant diseases</p>
        </div>
        <div className="steps-wrapper">
          <div className="steps-connector" />
          {[
            { n: 1, title: 'Upload Image', desc: 'Select a clear photo of the leaf from your device' },
            { n: 2, title: 'AI Analyzes', desc: 'Our deep learning model processes the image' },
            { n: 3, title: 'Disease Identified', desc: 'Get the disease name with confidence score' },
            { n: 4, title: 'View Suggestions', desc: 'Receive treatment and prevention recommendations' },
          ].map(({ n, title, desc }) => (
            <div className="step" key={n}>
              <div className="step-number">{n}</div>
              <h3>{title}</h3>
              <p>{desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section className="cta">
        <div className="cta-content">
          <h2>Ready to Protect Your Crops?</h2>
          <p>Start analyzing your leaf images now — it's free and instant.</p>
          <button className="btn btn-primary" onClick={() => onNavigate('predict')}>
            🌿 Get Started
          </button>
        </div>
      </section>

    </div>
  );
}

export default HomePage;
