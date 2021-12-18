import HomeScreen from './screens/HomeScreen';
import './App.css';
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import LoginScreen from './screens/LoginScreen';
import RegisterScreen from './screens/RegisterScreen';
import QuestionScreen from './screens/QuestionScreen';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<HomeScreen />} />
          <Route path="/login" element={<LoginScreen />} />
          <Route path="/register" element={<RegisterScreen />} />
          <Route path="/questions" element={<QuestionScreen />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
