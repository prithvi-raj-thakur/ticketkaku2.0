import React, { useState } from "react";
import "../css files/HelpChat.css";

const HelpChat = () => {
  const [messages, setMessages] = useState([
    { sender: "bot", text: "Hello 👋, I’m TicketKaku Help Bot. Please choose a category:" }
  ]);
  const [showCategories, setShowCategories] = useState(true);
  const [selectedCategory, setSelectedCategory] = useState(null);

  const categories = {
    "Booking": [
      { q: "How to book a ticket?", a: "You can book by selecting the place, date, and number of persons, then completing payment." },
      { q: "Can I cancel my booking?", a: "Yes, cancellations are possible up to 24 hours before the visit." }
    ],
    "Payment": [
      { q: "Which payment methods are accepted?", a: "We accept UPI, cards, and net banking." },
      { q: "Is there a refund policy?", a: "Refunds are processed within 5-7 working days." }
    ],
    "Account": [
      { q: "How do I create an account?", a: "Click on Sign Up, fill in your details, and verify via email." },
      { q: "How can I reset my password?", a: "Click on 'Forgot Password' and follow the steps." }
    ],
    "Support": [
      { q: "How to contact support?", a: "You can reach us through the Contact Us form or via email." },
      { q: "Do you offer live chat?", a: "Currently, we offer email and chat bot support only." }
    ],
    "General": [
      { q: "What is TicketKaku?", a: "TicketKaku is an AI-powered ticket booking platform for Kolkata attractions." },
      { q: "Which places are covered?", a: "Museums, parks, and popular tourist spots across Kolkata." }
    ]
  };

  const handleCategoryClick = (category) => {
    setMessages((prev) => [...prev, { sender: "user", text: category }]);
    setMessages((prev) => [...prev, { sender: "bot", text: `You chose ${category}. Here are some questions:` }]);
    setSelectedCategory(category);
    setShowCategories(false);
  };

  const handleQuestionClick = (q, a) => {
    setMessages((prev) => [
      ...prev,
      { sender: "user", text: q },
      { sender: "bot", text: a },
      { sender: "bot", text: "Was this helpful? (Yes/No)" }
    ]);
  };

  const handleHelpful = (response) => {
    setMessages((prev) => [
      ...prev,
      { sender: "user", text: response },
      { sender: "bot", text: "Thanks for your feedback 🙏" }
    ]);
  };

  return (
    <div className="helpchat-container">
      <div className="helpchat-header">TicketKaku Help Bot</div>
      <div className="helpchat-body">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text === "Was this helpful? (Yes/No)" ? (
              <div>
                {msg.text}
                <div className="option-btns">
                  <span className="option-btn" onClick={() => handleHelpful("Yes")}>Yes</span>
                  <span className="option-btn" onClick={() => handleHelpful("No")}>No</span>
                </div>
              </div>
            ) : (
              msg.text
            )}
          </div>
        ))}

        {showCategories && (
          <div className="options">
            {Object.keys(categories).map((cat, i) => (
              <span key={i} className="option-btn" onClick={() => handleCategoryClick(cat)}>{cat}</span>
            ))}
          </div>
        )}

        {selectedCategory && (
          <div className="options">
            {categories[selectedCategory].map((qa, i) => (
              <span key={i} className="option-btn" onClick={() => handleQuestionClick(qa.q, qa.a)}>
                {qa.q}
              </span>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default HelpChat;