import axios from 'axios';
import React from 'react';
import { useState } from 'react/cjs/react.development';
import NavBar from '../components/NavBar';
import WeatherCard from '../components/WeatherCard';

const WeatherScreen = () => {
  const [weather, setWeather] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const clickHandler = () => {
    navigator.geolocation.getCurrentPosition(async function (position) {
      setLoading(false);

      let lat = position.coords.latitude;
      let long = position.coords.longitude;

      const { data } = await axios.get(
        `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${long}&appid=8f366d853427d4ac7e53364ff5bfb620`
      );

      setWeather(data);
      setLoading(true);
    });
  };

  return (
    <>
      <NavBar />
      <div
        style={{
          marginTop: '80px',
          display: 'flex',
          alignItems: 'center',
          flexDirection: 'column',
        }}
      >
        <button onClick={clickHandler} className="weather__btn">
          Click here to know your weather
        </button>
        {error && <p>{error}</p>}
        {loading && (
          <div style={{ marginTop: '50px' }}>
            <WeatherCard data={weather} />
          </div>
        )}
      </div>
    </>
  );
};

export default WeatherScreen;
