import axios from 'axios';
import React, { useEffect, useState } from 'react';
import NavBar from '../components/NavBar';
import WeatherCard from '../components/WeatherCard';
import { useNavigate } from 'react-router-dom';

const lists = [
  'Barcelona',
  'London',
  'Kathmandu',
  'Pokhara',
  'Madrid',
  'Boston',
  'Agra',
  'Delhi',

  'Washington',
  'Springfield',
  'Franklin',
  'Greenville',
  'Biratnagar',
  'Morang',
  'Orion',
  'Fort Smith',
  'Fort Walton Beach',
  'Fort Wayne',
  'Fort Worth',
  'Frederick',
  'Fremont',
  'Fresno',
  'Fullerton',
  'Gainesville',
  'Garden Grove',
  'Garland',
  'Gastonia',
  'Gilbert',
  'Glendale',
  'Grand Prairie',
  'Grand Rapids',
  'Grayslake',

  'Greensboro',
  'Greenville',
  'Gulfport-Biloxi',
  'Hagerstown',
  'Hampton',
  'Harlingen',
  'Harrisburg',
  'Hartford',
  'Havre de Grace',
  'Hayward',
  'Hemet',
  'Henderson',
  'Hesperia',
  'Hialeah',
  'Hickory',
  'High Point',
  'Hollywood',
  'Honolulu',
  'Houma',
  'Houston',
  'Howell',
  'Huntington',
  'Huntington Beach',
  'Huntsville',
  'Independence',
  'Indianapolis',
  'Inglewood',
];

const HomeScreen = () => {
  const [city, setCity] = useState([]);
  const [loading, setLoading] = useState(false);
  const history = useNavigate();

  async function callWeather() {
    setLoading(true);
    const arr = [];
    const res1 = await axios.get(
      `https://api.openweathermap.org/data/2.5/weather?q=${
        lists[Math.floor(Math.random() * lists.length)]
      }&appid=${process.env.API_KEY}`
    );
    arr.push(res1.data);
    const res2 = await axios.get(
      `https://api.openweathermap.org/data/2.5/weather?q=${
        lists[Math.floor(Math.random() * lists.length)]
      }&appid=${process.env.API_KEY}`
    );
    arr.push(res2.data);
    const res3 = await axios.get(
      `https://api.openweathermap.org/data/2.5/weather?q=${
        lists[Math.floor(Math.random() * lists.length)]
      }&appid=${process.env.API_KEY}`
    );
    arr.push(res3.data);

    setLoading(false);
    setCity(arr);
  }
  useEffect(() => {
    callWeather();
  }, []);

  return (
    <div>
      <NavBar />
      <h1 style={{ textAlign: 'center' }}>Weather Data</h1>
      <div className="container">
        {loading ? (
          <h1>Loading...</h1>
        ) : (
          <>
            {city.map((el) => (
              <WeatherCard key={el.name} data={el} />
            ))}
          </>
        )}
        <div
          style={{ display: 'flex', justifyContent: 'center', width: '100%' }}
        >
          <button
            onClick={() => history('/questions')}
            className="weather__btn"
          >
            Flood Risk Assessment
          </button>
        </div>
      </div>
    </div>
  );
};

export default HomeScreen;
