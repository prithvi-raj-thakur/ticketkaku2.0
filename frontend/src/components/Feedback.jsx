import React from "react";
import "../css files/Feedback.css";
import { feedbacks } from "../assets/assets";



const Feedback = () => {
  return (
    <section id="feedback" className="feedback-section">
      <h1>Feedbacks</h1>
      <div className="feedback-container">
        {feedbacks.map((item, index) => (
          <div className="feedback-card" key={index}>
            <img src={item.img} alt={item.name} />
            <h3>{item.name}</h3>
            <p className="feedback-text">{item.text}</p>
            <div className="rating">{item.rating}</div>
            <p className="review-date">{item.date}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Feedback;