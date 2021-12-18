import React from 'react';
import '../styles/weathercard.css';
import { ReactComponent as Sun } from '../icons/sun.svg';
import { ReactComponent as Cloud } from '../icons/cloud.svg';
import { ReactComponent as Rain } from '../icons/rain.svg';
import { ReactComponent as Haze } from '../icons/haze.svg';
import { ReactComponent as Thunder } from '../icons/thunderstorm.svg';
import { ReactComponent as Wind } from '../icons/wind.svg';

const WeatherCard = ({ data }) => {
  console.log(data);
  return (
    <div className="weather__card">
      <>
        <div
          style={{
            display: 'flex',
            justifyContent: 'center',
          }}
        >
          {data.weather[0].main === 'Clear' ? (
            <Sun className="icons" />
          ) : data.weather[0].main === 'Clouds' ? (
            <Cloud className="icons" />
          ) : data.weather[0].main === 'Rain' ? (
            <Rain className="icons" />
          ) : data.weather[0].main === 'thunder' ? (
            <Thunder className="icons" />
          ) : data.weather[0].main === 'Mist' ? (
            <Wind className="icons" />
          ) : (
            <Haze className="icons" />
          )}
        </div>
        <p>Temperature: {data?.main?.temp} K</p>
        <p>City: {data.name}</p>
        <p>Status: {data.weather[0].description}</p>
        <p>Humidity: {data.main.humidity}</p>
      </>
    </div>
  );
};

export default WeatherCard;
