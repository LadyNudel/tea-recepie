import { useState, useEffect } from "react";
import { wait, getRandomBetween } from "./util";

function useTyping(text, min, max) {
  let [typing, setTyping] = useState("");
  useEffect(() => {
    async function startTyping() {
      for (const letter of text) {
        setTyping(state => state + letter);
        await wait(getRandomBetween(min, max));
      }
    }
    startTyping();
  }, [text, min, max]);
  return typing;
}

export default useTyping;
