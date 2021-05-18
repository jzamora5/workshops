import React from 'react';

const RickAndMortyCharacters = ({ characters }) => {
  console.log(characters);

  return (
    <>
      {!characters.length && <h1>Loading....</h1>}
      {characters.map((character) => {
        return <h1 key={character.id}>{character.name}</h1>;
      })}
    </>
  );
};

export default RickAndMortyCharacters;
