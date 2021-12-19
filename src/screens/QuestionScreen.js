import axios from 'axios';
import React, { useEffect } from 'react';
import { useState } from 'react/cjs/react.development';
import { api } from '../api';
import NavBar from '../components/NavBar';

const QuestionScreen = () => {
  const [number, setNumber] = useState(1);
  const [question, setQuestion] = useState({});
  const [loading, setLoading] = useState(false);
  const [answer, setAnswer] = useState();
  const [result, setResult] = useState('');

  const sendEmail = async (ans) => {
    const token = localStorage.getItem('token');
    let config = {
      headers: {
        Authorization: 'Bearer ' + token,
      },
    };
    await axios.post(`${api}/send-email/`, { body: ans }, config);
  };

  const fetchQuestion = async () => {
    const token = localStorage.getItem('token');
    setLoading(true);
    let config = {
      headers: {
        Authorization: 'Bearer ' + token,
      },
    };
    const res = await axios.get(`${api}/getq/${number}`, config);

    setQuestion(res.data);
    setLoading(false);
  };
  useEffect(() => {
    fetchQuestion();
  }, [number]);

  const submitHandler = async () => {
    const token = localStorage.getItem('token');

    let config = {
      headers: {
        Authorization: 'Bearer ' + token,
      },
    };
    await axios.post(`${api}/storeans/${question.id}`, { answer }, config);
    if (answer === true && isNaN(question.yes)) {
      sendEmail(`You are at ${question.yes} risk`);
      return setResult(question.yes);
    }
    if (answer === false && isNaN(question.no)) {
      sendEmail(`You are at ${question.no} risk`);
      return setResult(question.no);
    }

    setNumber(answer === true ? Number(question.yes) : Number(question.no));
  };
  console.log(number);
  return (
    <div>
      <NavBar />
      {loading ? (
        <p>Loading.....</p>
      ) : (
        <>
          {!result && (
            <>
              <p>Step {number}</p>
              <p>Q: {question.question} </p>
              <label>Yes</label>
              <input onChange={() => setAnswer(true)} name="r1" type="radio" />
              <label>No</label>
              <input onChange={() => setAnswer(false)} name="r1" type="radio" />
              <button onClick={submitHandler}>Submit</button>
            </>
          )}

          {result && (
            <p style={{ textAlign: 'center', marginTop: '40px' }}>
              You are at {result} Risk
            </p>
          )}
        </>
      )}
    </div>
  );
};

export default QuestionScreen;
