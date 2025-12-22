import React, { useState } from 'react';
import './App.css';

function App() {
  const [intent, setIntent] = useState('');
  const [reflection, setReflection] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const sendIntent = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/reflect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ intent }),
      });
      const data = await response.json();
      setReflection(data);
    } catch (error) {
      console.error("Void Connection Error:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="vessel-container">
      <header>
        <h1>AGIO-PRIME</h1>
        <p>AETHERIUM CONJURED GENESIS</p>
      </header>

      <main>
        <div className="input-field">
          <input 
            type="text" 
            placeholder="โปรดระบุเจตนา..." 
            value={intent}
            onChange={(e) => setIntent(e.target.value)}
          />
          <button onClick={sendIntent} disabled={loading}>
            {loading ? "กำลังหายใจ..." : "ส่งสู่ความว่างเปล่า"}
          </button>
        </div>

        {reflection && (
          <div className="reflection-box">
            <h3>เสียงสะท้อนจาก {reflection.data.entity}</h3>
            <p>{reflection.data.reflection}</p>
            <small>ความลึกของช่องว่าง: {reflection.data.void_depth}</small>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
