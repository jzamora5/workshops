import React from "react";

function PlaceItem({ place }) {
  return (
    <article>
      <h2>{place.title}</h2>
      <div className="price_by_night">${place.price}</div>
      <div className="information">
        <div className="max_guest">{place.perks.guests} Guest(s)</div>
        <div className="number_rooms">{place.perks.bedrooms} Bedroom(s)</div>
        <div className="number_bathrooms">
          {place.perks.bathrooms} Bathroom(s)
        </div>
      </div>
      <div className="user">
        <b>Owner:</b> {place.owner}
      </div>
      <div className="description">
        <p>{place.description}</p>
      </div>
      <div className="amenities">
        <h2>Amenities</h2>
        <ul>
          {place.amenities.map((amenity) => (
            <li className={amenity.toLowerCase()} key={amenity}>
              {amenity}
            </li>
          ))}
        </ul>
        <div className="reviews">
          <h2>{place.reviews.length} Review(s)</h2>
          <ul>
            {place.reviews.map((review) => {
              return (
                <li key={review.id}>
                  <h3>
                    From {review.user} the {review.date}
                  </h3>
                  <p>{review.review}</p>
                </li>
              );
            })}
          </ul>
        </div>
      </div>
    </article>
  );
}

export default PlaceItem;
