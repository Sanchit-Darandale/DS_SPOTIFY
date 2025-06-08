import React from 'react';
import axios from 'axios';

const DownloadButton = ({ title }) => {
  const handleDownload = async () => {
    try {
      const apiUrl = import.meta.env.VITE_API_URL || '/api';
      const res = await axios.get(`${apiUrl}/download?query=${encodeURIComponent(title)}`);
      window.open(res.data.url, '_blank');
    } catch (err) {
      alert("Download failed.");
    }
  };

  return <button onClick={handleDownload}>Download</button>;
};

export default DownloadButton;
