import getPokemon from "./utils/getPokemon.js";
import createCard from "./utils/createCard.js";

const app = document.getElementById("app");

async function showPokemon() {
  const pokemons = await getPokemon();

  pokemons.forEach((pokemon) => {
    const cardData = {
      picture: pokemon.picture,
      title: pokemon.name,
      body: pokemon.number,
      list: pokemon.types,
    };

    const pokemonCard = createCard(cardData);
    app.append(pokemonCard);
  });
}

showPokemon();
