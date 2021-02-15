import { getData } from "../api/crud.js";

const pokemonsURL = "https://pokeapi.co/api/v2/pokemon/?limit=151";

async function getPokemon() {
  const pokemonList = await getData(pokemonsURL);

  const pokemonDataList = [];

  for (const pokemon of pokemonList.results) {
    const pokemonData = await getData(pokemon.url);
    const {
      id: number,
      name,
      types,
      sprites: { front_default: picture },
    } = pokemonData;

    pokemonDataList.push({
      number,
      name,
      types,
      picture,
    });
  }

  return pokemonDataList;
}

export default getPokemon;
