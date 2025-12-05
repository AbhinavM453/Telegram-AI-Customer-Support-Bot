import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [messages, setMessages] = useState([]);
  const [userMessage, setUserMessage] = useState("");

  
  const API_BASE = "http://localhost:8000"; 

  
  const fetchMessages = async () => {
    const res = await axios.get(`${API_BASE}/bot/messages/`);
    setMessages(res.data);
  };

  useEffect(() => {
    fetchMessages();
  }, []);

  
  const sendMessage = async (e) => {
    e.preventDefault();
    await axios.post(`${API_BASE}/bot/test-send/`, {
      message: userMessage
    });
    setUserMessage("");
    fetchMessages();
  };

  return (
    <div style={{ width: "600px", margin: "auto", padding: "20px" }}>
      <h2>Telegram AI Customer Support Dashboard</h2>

      <form onSubmit={sendMessage}>
        <input
          type="text"
          placeholder="Send a test message"
          value={userMessage}
          onChange={(e) => setUserMessage(e.target.value)}
          style={{ width: "80%", padding: "10px" }}
        />
        <button type="submit" style={{ padding: "10px" }}>
          Send
        </button>
      </form>

      <h3 style={{ marginTop: "20px" }}>Chat History</h3>
      <div style={{ border: "1px solid #ccc", padding: "10px" }}>
        {messages.map((msg, index) => (
          <div key={index} style={{ marginBottom: "15px" }}>
            <p><strong>User:</strong> {msg.message}</p>
            <p><strong>AI:</strong> {msg.response}</p>
            <hr />
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
