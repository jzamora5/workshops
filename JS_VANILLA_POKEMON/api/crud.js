export async function getData(URL) {
  const response = await fetch(URL);

  const body = await response.json();

  return body;
}
