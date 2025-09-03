import React from "react";
import { useNavigate } from "react-router-dom";
import {museumData} from "../assets/assets.js";
import "../css files/Museum.css"

const Museum = () => {
  const navigate = useNavigate();

  return (
    <div className="flashcards-container">
      {museumData.map((item) => (
        <div
          className="flashcard"
          key={item.id}
          onClick={() => navigate(`/museum/${item.id}`)} // navigate to details page
        >
          <img src={item.image} alt={item.name} className="flashcard-img" />
          <div className="flashcard-content">
            <h3>{item.name}</h3>
            <p>{item.description}</p>
            <span className="price">₹{item.price}</span>
          </div>
        </div>
      ))}
    </div>
  );
};

export default Museum;