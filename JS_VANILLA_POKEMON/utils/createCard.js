function createCard(cardData) {
  const card = document.createElement("div");
  card.className = "card";

  card.addEventListener("click", () => {
    console.log(cardData.title);
  });

  const cardPicture = document.createElement("img");
  cardPicture.src = cardData.picture;
  card.append(cardPicture);

  const cardTitle = document.createElement("h3");
  cardTitle.innerText = cardData.title;
  card.append(cardTitle);

  const cardBody = document.createElement("p");
  cardBody.innerText = `# ${cardData.body}`;
  card.append(cardBody);

  const cardList = document.createElement("ul");

  cardData.list.forEach((item) => {
    const cardListItem = document.createElement("li");
    cardListItem.innerText = item.type.name;
    cardList.append(cardListItem);
  });

  card.append(cardList);

  return card;
}

export default createCard;
