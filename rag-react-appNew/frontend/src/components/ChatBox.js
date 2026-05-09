import React, { useState } from "react";
import { askQuestion } from "../api/ragApi";

export default function ChatBox() {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    const trimmedQuery = query.trim();
    if (!trimmedQuery || loading) return;

    const userMsg = { role: "user", text: trimmedQuery };
    setMessages(prev => [...prev, userMsg]);

    setQuery("");
    setLoading(true);

    try {
      const res = await askQuestion(trimmedQuery);

      const botMsg = {
        role: "bot",
        text: res?.answer || "No answer returned.",
      };

      setMessages(prev => [...prev, botMsg]);
    } catch (err) {
      setMessages(prev => [
        ...prev,
        { role: "bot", text: "Error: Unable to fetch response." }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>RAG Chat</h2>

      <div style={{ marginBottom: 20 }}>
        {messages.map((m, i) => (
          <p key={i}>
            <b>{m.role}:</b> {m.text}
          </p>
        ))}
      </div>

      <input
        value={query}
        onChange={e => setQuery(e.target.value)}
        onKeyDown={e => {
          if (e.key === "Enter") handleSend();
        }}
        placeholder="Ask a question..."
        style={{ marginRight: 10 }}
      />

      <button onClick={handleSend} disabled={loading}>
        {loading ? "Sending..." : "Send"}
      </button>
    </div>
  );
}