import React from 'react';

const Player = ({ track }) => {
  return track.preview_url ? (
    <audio controls src={track.preview_url}></audio>
  ) : (
    <p>Preview not available</p>
  );
};

export default Player;
