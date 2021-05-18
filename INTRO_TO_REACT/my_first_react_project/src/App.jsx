import { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import MyComponent from './components/MyComponent';
import RickAndMortyCharacters from './components/RickAndMortyCharacters';

const URL = 'https://rickandmortyapi.com/api/character';

function App() {
  const [myColor, setMyColor] = useState('red');
  const [characters, setCharacters] = useState([]);

  const requestCharacters = async () => {
    console.log('Requesting');
    const response = await fetch(URL);
    const body = await response.json();
    const { results: characters } = body;
    setCharacters(characters);
  };

  useEffect(() => {
    requestCharacters();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p className={myColor}>My First React App</p>
        <br />
        <MyComponent
          name={'Larry'}
          lastName={'Hudson'}
          myColor={myColor}
          setMyColor={setMyColor}
        />
        <RickAndMortyCharacters characters={characters} />
      </header>
    </div>
  );
}

export default App;
