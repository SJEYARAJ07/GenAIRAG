import React, { useState } from "react";
import { askQuestion } from "../api/ragApi";

export default function ChatBox() {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]);

  const handleSend = async () => {
    if (!query) return;

    const userMsg = { role: "user", text: query };
    setMessages(prev => [...prev, userMsg]);

    const res = await askQuestion(query);

    const botMsg = { role: "bot", text: res.answer };
    setMessages(prev => [...prev, userMsg, botMsg]);

    setQuery("");
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>RAG Chat</h2>

      <div>
        {messages.map((m, i) => (
          <p key={i}><b>{m.role}:</b> {m.text}</p>
        ))}
      </div>

      <input value={query} onChange={e => setQuery(e.target.value)} />
      <button onClick={handleSend}>Send</button>
    </div>
  );
}