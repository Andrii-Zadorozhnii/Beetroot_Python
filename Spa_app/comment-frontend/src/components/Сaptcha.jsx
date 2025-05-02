import { useEffect, useState } from 'react';
import api from '../api/axios';

export default function Captcha({ onChange }) {
  const [captcha, setCaptcha] = useState(null);

  useEffect(() => {
    fetchCaptcha();
  }, []);

  const fetchCaptcha = async () => {
    try {
      const res = await api.get('captcha/');
      setCaptcha(res.data);
      onChange({ key: res.data.captcha_key, text: '' });
    } catch (err) {
      console.error('Failed to load CAPTCHA:', err);
    }
  };

  const handleInput = (e) => {
    onChange(prev => ({ ...prev, text: e.target.value }));
  };

  return (
    <div>
      {captcha && (
        <>
          <img src={`http://localhost:8000${captcha.image_url}`} alt="captcha" />
          <input
            type="text"
            placeholder="Enter CAPTCHA"
            onChange={handleInput}
          />
          <button type="button" onClick={fetchCaptcha}>⟳ Refresh</button>
        </>
      )}
    </div>
  );
}