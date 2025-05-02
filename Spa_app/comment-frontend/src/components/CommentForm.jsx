import { useState } from 'react';
import api from '../api/axios';
import Captcha from "./Сaptcha";

export default function CommentForm() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    homepage: '',
    text: '',
    captcha_key: '',
    captcha_text: '',
  });

  const [captchaData, setCaptchaData] = useState({});
  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    setFormData(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }));
  };

  const handleCaptchaChange = ({ key, text }) => {
    setCaptchaData({ key, text });
    setFormData(prev => ({
      ...prev,
      captcha_key: key,
      captcha_text: text,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post('comments/', formData);
      setMessage('Комментарий отправлен!');
      setFormData({
        username: '',
        email: '',
        homepage: '',
        text: '',
        captcha_key: '',
        captcha_text: '',
      });
    } catch (err) {
      console.error(err);
      setMessage('Ошибка при отправке комментария.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="username" placeholder="Name" value={formData.username} onChange={handleChange} required />
      <input name="email" placeholder="Email" type="email" value={formData.email} onChange={handleChange} required />
      <input name="homepage" placeholder="Homepage (optional)" value={formData.homepage} onChange={handleChange} />
      <textarea name="text" placeholder="Your comment" value={formData.text} onChange={handleChange} required />
      <Captcha onChange={handleCaptchaChange} />
      <button type="submit">Отправить</button>
      {message && <p>{message}</p>}
    </form>
  );
}