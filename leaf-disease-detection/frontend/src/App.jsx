import { useState } from 'react';
import './App.css';
import HomePage from './pages/HomePage';
import PredictionPage from './pages/PredictionPage';
import AboutPage from './pages/AboutPage';

function App() {
  const [currentPage, setCurrentPage] = useState('home');
  const [pageKey, setPageKey] = useState(0);

  const navigate = (page) => {
    setCurrentPage(page);
    setPageKey(k => k + 1);
  };

  return (
    <div className="App">
      <nav className="navbar">
        <div className="navbar-container">
          <div className="logo">
            <span className="logo-icon">🌿</span>
            Leaf Disease Detection
          </div>
          <ul className="nav-menu">
            <li><button onClick={() => navigate('home')} className={currentPage === 'home' ? 'active' : ''}>Home</button></li>
            <li><button onClick={() => navigate('predict')} className={currentPage === 'predict' ? 'active' : ''}>Predict</button></li>
            <li><button onClick={() => navigate('about')} className={currentPage === 'about' ? 'active' : ''}>About</button></li>
          </ul>
        </div>
      </nav>

      <main className="main-content">
        <div key={pageKey} className="page-enter">
          {currentPage === 'home' && <HomePage onNavigate={navigate} />}
          {currentPage === 'predict' && <PredictionPage />}
          {currentPage === 'about' && <AboutPage />}
        </div>
      </main>

      <footer className="footer">
        <p>© 2024 Leaf Disease Detection System · Powered by AI</p>
      </footer>
    </div>
  );
}

export default App;
