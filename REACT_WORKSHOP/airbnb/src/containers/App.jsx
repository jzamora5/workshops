import React, { useState, useEffect } from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
import Filters from "../components/Filters";
import Places from "../components/Places";
import "../assets/styles/App.css";

// const initialState = [
//   {
//     title: "My Home",
//     price: 80,
//     perks: { guests: 2, bedrooms: 1, bathrooms: 1 },
//     owner: "Johnny",
//     description:
//       "This is a lovely 1 bedroom and 1 bathroom apartment that can accommodate 2 people. It locates at the center of Shanghai and next to subway line 1,1 stop to People Square, 2 stops to Bund, 3 stops to Jingan Temple.",
//     amenities: ["TV", "Wifi", "Pets"],
//     reviews: [
//       {
//         user: "Bob Dylan",
//         date: "27th January 2017",
//         review: "Runshi is an epic host. Nothing more I can say. 5 star!",
//       },
//       {
//         user: "Connor",
//         date: "4th January 2017",
//         review: "Highly recommended!",
//       },
//     ],
//   },
//   {
//     title: "Tiny House",
//     price: 65,
//     perks: { guests: 4, bedrooms: 2, bathrooms: 1 },
//     owner: "Adrienne",
//     description:
//       "Our place is a private, affordable stand-alone guest house centrally located just minutes to French Quarters, downtown, the Fair Grounds(Jazz Fest) and City Park. The guest house is a quaint, 400 square ft. with a full bath, mini kitchen, & living room. The extra high ceilings make the home feel more spacious. The sofa converts to a bed also. We have a hand made counter area that adds character to the room and a great porch/deck to relax on and have a glass of Merlot.",
//     amenities: ["Pets"],
//     reviews: [
//       {
//         user: "Max",
//         date: "15th January 2017",
//         review:
//           "Fantastic place. It was clean, Adrienne was great (even though we did not meet in person) and everything went super smooth. Location is also greate if you like running and something a bit more quiet. I would suggest a car or take into consideration that you might have to Uber into the city from the location. Overall, would recommend the place anytime.",
//       },
//     ],
//   },
//   {
//     title: "A suite",
//     price: 190,
//     perks: { guests: 4, bedrooms: 4, bathrooms: 3 },
//     owner: "Lue",
//     description:
//       "This is a premium quality room located in the most important area of New York. It is close to downtown commerces and has a beatiful sight of central park. You will have all the amenities you desire and will definitely enjoy a great time. By yourself, with your lover, or your family, you will feel luxury from top to bottom.",
//     amenities: ["TV", "Wifi"],
//     reviews: [
//       {
//         user: "Kamie Nean",
//         date: "6th September 2017",
//         review: "I felt like a Queen during my stay!",
//       },
//       {
//         user: "Heman",
//         date: "5th October 2017",
//         review: "Beautiful Place.",
//       },
//       {
//         user: "Numa",
//         date: "15th August 2017",
//         review: "Great view and service!",
//       },
//     ],
//   },
// ];

const URL = "http://localhost:8000/places/";

// let placesList = [];

/* 
 Variables by themselves only change bits in memory and the state of your app can get out of sync with the view. 
 In both cases a variable can chance on click but only when you use useState the view correctly shows the variables 's current value. 
 Updating state will make the component to re-render again, but local values are not.
*/

function App() {
  const [placesList, setPlacesList] = useState([]);

  /* When you run your application, you should stumble into a nasty loop. 
  The effect hook runs when the component mounts but also when the component updates. 
  Because we are setting the state after every data fetch, the component updates and the effect runs again. 
  It fetches the data again and again. That's a bug and needs to be avoided. 
  We only want to fetch data when the component mounts.
   That's why you can provide an empty array as second argument to the effect hook 
   to avoid activating it on component updates but only for the mounting of the component. 


   For solving this, we pass a second argument to useEffect so that it only runs on component mount

   The second argument can be used to define all the variables (allocated in this array) on which the hook depends.
   If one of the variables changes, the hook runs again. If the array with the variables is empty, the hook doesn't 
   run when updating the component at all, because it doesn't have to watch any variables.

   */

  useEffect(() => {
    //
    (async () => {
      const response = await fetch(URL);
      const places = await response.json();
      setPlacesList(places);
    })();

    // fetch(URL)
    //   .then((response) => response.json())
    //   .then((places) => setPlacesList(places));

    console.log("useEffect");
  }, []);

  return (
    <>
      <Header />
      <div className="App container">
        <Filters />
        <Places placesList={placesList} />
      </div>
      <Footer />
    </>
  );
}

export default App;

// json-server --watch db.json --port 8000
