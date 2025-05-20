import React, { useState } from "react";
import Sidebar from "./components/Sidebar.jsx";
import ChatLayout from "./components/ChatLayout.jsx";
import CodeForm from "./components/CodeForm.jsx";
import "./style.css";

const App = () => {
  const [history, setHistory] = useState([]);
  const [generatedCode, setGeneratedCode] = useState("");

  const handleGenerate = async (prompt, language) => {
    const res = await fetch("http://localhost:8000/generate/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt, language }),
    });
    const data = await res.json();
    setGeneratedCode(data.generated_code);
    setHistory((prev) => [...prev, { prompt, code: data.generated_code }]);
  };

  return (
    <div className="container">
      <Sidebar history={history} />
      <ChatLayout>
        <CodeForm onGenerate={handleGenerate} />
        <pre>
          <code>{generatedCode}</code>
        </pre>
      </ChatLayout>
    </div>
  );
};

export default App;
