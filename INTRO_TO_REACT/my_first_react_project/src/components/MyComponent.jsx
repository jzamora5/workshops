import React from 'react';

const MyComponent = (props) => {
  const handleClick = () => {
    if (props.myColor === 'red') props.setMyColor('blue');
    else props.setMyColor('red');
  };

  return (
    <>
      <h1>
        Hello {props.name} {props.lastName}
      </h1>
      <button onClick={handleClick}>Change Color</button>
    </>
  );
};

export default MyComponent;
