import React from "react";
import useMyHook from "use-typing-hook";

const App = () => {
  const typing = useMyHook("Hello React Typing Hook!");
  return <h1>{typing}</h1>;
};
export default App;
