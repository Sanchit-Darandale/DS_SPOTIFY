import React, { useState } from 'react';
import axios from 'axios';

const SearchBar = ({ setTrack }) => {
  const [query, setQuery] = useState('');

  const handleSearch = async () => {
    try {
      const apiUrl = import.meta.env.VITE_API_URL || '/api';
      const res = await axios.get(`${apiUrl}/search?q=${query}`);
      const track = res.data.tracks?.items?.[0];
      if (!track) return alert("No results found");
      setTrack(track);
    } catch (e) {
      alert('Error searching Spotify');
    }
  };

  return (
    <div>
      <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Search track" />
      <button onClick={handleSearch}>Search</button>
    </div>
  );
};

export default SearchBar;
