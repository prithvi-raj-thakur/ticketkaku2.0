import React, { useState } from "react";
import axios from "axios";
import { Paperclip, Send } from "lucide-react"; // nice icons

function Chatbot() {
  const [messages, setMessages] = useState([
    { sender: "bot", text: "👋 Hi! I'm TicketKaku – your Kolkata guide & booking assistant." }
  ]);
  const [input, setInput] = useState("");
  const [file, setFile] = useState(null);

  // Send message to backend
  const sendMessage = async () => {
    if (!input.trim()) return;

    const newMessages = [...messages, { sender: "user", text: input }];
    setMessages(newMessages);

    try {
      const response = await axios.post("http://localhost:5000/chat", {
        message: input,
      });
      setMessages([...newMessages, { sender: "bot", text: response.data.reply }]);
    } catch (error) {
      setMessages([
        ...newMessages,
        { sender: "bot", text: "⚠ Error connecting to server. Please try again later." }
      ]);
    }

    setInput("");
  };

  // Handle Enter key
  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      sendMessage();
    }
  };

  // Handle File Upload
  const handleFileUpload = (e) => {
    setFile(e.target.files[0]);
  };

  return (
    <div className="h-screen w-screen flex flex-col bg-gray-100">
      
      {/* Header */}
      <div className="bg-blue-600 text-white text-lg font-semibold px-4 py-3 shadow-md flex items-center">
        🎟 TicketKaku Chatbot
      </div>

      {/* Chat Window */}
      <div className="flex-1 overflow-y-auto p-4 space-y-3">
        {messages.map((msg, i) => (
          <div key={i} className={`flex ${msg.sender === "user" ? "justify-end" : "justify-start"}`}>
            {msg.sender === "bot" && (
              <div className="w-8 h-8 rounded-full bg-gray-400 flex items-center justify-center mr-2">
                🤖
              </div>
            )}
            <div
              className={`max-w-xs md:max-w-md px-4 py-2 rounded-2xl shadow ${
                msg.sender === "user"
                  ? "bg-blue-500 text-white rounded-br-none"
                  : "bg-gray-200 text-gray-800 rounded-bl-none"
              }`}
            >
              {msg.text}
            </div>
            {msg.sender === "user" && (
              <div className="w-8 h-8 rounded-full bg-blue-500 text-white flex items-center justify-center ml-2">
                👤
              </div>
            )}
          </div>
        ))}
      </div>

      {/* Input Area */}
      <div className="p-3 border-t bg-white flex items-center gap-2">
        {/* File Upload */}
        <label className="cursor-pointer">
          <input
            type="file"
            className="hidden"
            onChange={handleFileUpload}
          />
          <Paperclip className="text-gray-500 hover:text-blue-600 w-6 h-6" />
        </label>
        {file && <span className="text-xs text-gray-500 truncate max-w-[100px]">📂 {file.name}</span>}

        {/* Text Input */}
        <input
          type="text"
          className="flex-1 border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
          placeholder="Type your message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
        />

        {/* Send Button */}
        <button
          onClick={sendMessage}
          className="bg-blue-600 text-white p-2 rounded-lg hover:bg-blue-700 flex items-center justify-center"
        >
          <Send className="w-5 h-5" />
        </button>
      </div>
    </div>
  );
}

export default Chatbot;