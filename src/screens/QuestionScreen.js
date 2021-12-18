import axios from 'axios';
import React, { useEffect } from 'react';
import { useState } from 'react/cjs/react.development';
import { api } from '../api';
import NavBar from '../components/NavBar';

const QuestionScreen = () => {
  const [number, setNumber] = useState(1);
  const [question, setQuestion] = useState({});

  const fetchQuestion = async () => {
    const token = localStorage.getItem('token');

    let config = {
      headers: {
        Authorization: 'Bearer ' + token,
      },
    };
    const res = await axios.get(`${api}/getq/${number}`, config);
    setQuestion(res.data);
    console.log(res.data);
  };
  useEffect(() => {
    fetchQuestion();
  }, [number]);
  return (
    <div>
      <NavBar />
      <p>Q: {question.question} </p>
    </div>
  );
};

export default QuestionScreen;
