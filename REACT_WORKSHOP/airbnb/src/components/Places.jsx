import React from "react";
import PlaceItem from "./PlaceItem";
import "../assets/styles/components/Places.css";

function Places({ placesList }) {
  return (
    <section className="places">
      <h1>Places</h1>
      {placesList.map((place) => (
        <PlaceItem place={place} key={place.id} />
      ))}
    </section>
  );
}

export default Places;
