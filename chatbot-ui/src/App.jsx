import React, { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!query.trim()) return;

    setLoading(true);
    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: query }),
      });

      const data = await res.json();
      setResponse(data.response);
    } catch (err) {
      console.error(err);
      setResponse("Error connecting to the chatbot.");
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    sendMessage();
  };

  return (
    <div className="flex items-center justify-center h-screen bg-gradient-to-r from-blue-500 to-purple-600">
      <div className="bg-white p-8 rounded-xl shadow-xl max-w-lg w-full text-black">
        <h1 className="text-2xl font-bold mb-4 text-center">💬 Chat with Support</h1>
        <form onSubmit={handleSubmit} className="flex gap-2 mb-4">
          <input
            className="flex-1 border rounded px-4 py-2"
            type="text"
            placeholder="Type your message..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <button
            type="submit"
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
          >
            Send
          </button>
        </form>
        <div className="min-h-[80px] bg-gray-100 rounded p-4">
          {loading ? (
            <p className="text-gray-500 italic">Thinking...</p>
          ) : (
            response && <p>{response}</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;

