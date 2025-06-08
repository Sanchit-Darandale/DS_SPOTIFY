import React, { useState } from 'react';
import SearchBar from './components/SearchBar';
import Player from './components/Player';
import DownloadButton from './components/DownloadButton';

const App = () => {
  const [track, setTrack] = useState(null);

  return (
    <div>
      <h1>Spotify Dashboard</h1>
      <SearchBar setTrack={setTrack} />
      {track && (
        <>
          <h2>{track.name} - {track.artists[0].name}</h2>
          <Player track={track} />
          <DownloadButton title={track.name + ' ' + track.artists[0].name} />
        </>
      )}
    </div>
  );
};

export default App;
