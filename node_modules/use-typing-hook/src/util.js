export function getRandomBetween(
  min = 20,
  max = 150,
  randomNumber = Math.random()
) {
  return Math.floor(randomNumber * (max - min) + min);
}
export function wait(time) {
  return new Promise(resolve => setTimeout(resolve, time));
}
