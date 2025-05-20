import React, { useState } from "react";

const CodeForm = ({ onGenerate }) => {
  const [prompt, setPrompt] = useState("");
  const [language, setLanguage] = useState("python");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (prompt.trim() === "") return;
    onGenerate(prompt, language);
    setPrompt("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        placeholder="Opisz co chcesz wygenerować..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <select
        value={language}
        onChange={(e) => setLanguage(e.target.value)}
      >
        <option value="python">Python</option>
        <option value="cpp">C++</option>
        <option value="java">Java</option>
      </select>
      <button type="submit">Generuj kod</button>
    </form>
  );
};

export default CodeForm;
