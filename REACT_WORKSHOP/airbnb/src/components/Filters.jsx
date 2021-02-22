import React from "react";
import "../assets/styles/components/Filters.css";

function Filters() {
  return (
    <section className="filters">
      <button>Search</button>
      <div className="locations">
        <h3>States</h3>
        <h4>California, Arizona...</h4>
        <ul className="popover">
          <li>
            <h2>Arizona:</h2>
          </li>
          <li>
            <ul>
              <li>Phoenix</li>
              <li>Tucson</li>
            </ul>
          </li>
          <li>
            <h2>California:</h2>
          </li>
          <li>
            <ul>
              <li>San Francisco</li>
              <li>Los Altos</li>
            </ul>
          </li>
        </ul>
      </div>
      <div className="amenities">
        <h3>Amenities</h3>
        <h4>Internet, Kitchen...</h4>
        <ul className="popover">
          <li>Internet</li>
          <li>TV</li>
          <li>Kitchen</li>
          <li>Iron</li>
        </ul>
      </div>
    </section>
  );
}

export default Filters;
