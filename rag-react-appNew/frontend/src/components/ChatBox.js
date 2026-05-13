import React, { useEffect, useRef, useState } from "react";
import { askQuestion } from "../api/ragApi";

export default function ChatBox() {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([
    { role: "bot", text: "Hi" },
  ]);
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const handleSend = async () => {
    const trimmed = query.trim();
    if (!trimmed || loading) return;

    setMessages((prev) => [...prev, { role: "user", text: trimmed }]);
    setQuery("");
    setLoading(true);

    try {
      const res = await askQuestion(trimmed);
      const botText = res?.answer || res?.result || "No answer returned.";

      setMessages((prev) => [...prev, { role: "bot", text: botText }]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "bot", text: "Error getting response" },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-bg">
      <div className="chat-container">
        <h1 className="title">POC Portfolio Delivery Intelligence</h1>
        <p className="subtitle">
          Ask a question based on the loaded context.
        </p>

        <div className="chat-area">
          {messages.map((m, i) => (
            <div key={i} className={`msg ${m.role}`}>
              {m.text}
            </div>
          ))}

          {loading && <div className="msg bot thinking">Thinking...</div>}

          <div ref={messagesEndRef} />
        </div>

        <div className="input-row">
          <input
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Ask your question..."
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
          />
          <button onClick={handleSend} disabled={loading}>
            Ask
          </button>
        </div>
      </div>
    </div>
  );
}
