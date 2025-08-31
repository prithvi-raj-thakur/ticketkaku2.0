import React from "react";
import Slider from "react-slick";
import {museumData} from "../assets/assets"; 
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import "../css files/OwlCarousel.css"; 
import { useNavigate } from "react-router-dom";


const OwlCarousel = () => {
   const settings = {
    infinite: true,        
    slidesToShow: 3,       
    centerMode: true,
    centerPadding: "0px",  
    autoplay: true,
    autoplaySpeed: 2500,   
    speed: 1000,           
    arrows: true,
    dots: false,
    pauseOnHover: false,   
    cssEase: "linear",
  };

  const navigate = useNavigate();
  

  return (
    <div className="carousel-container">
      <h2 className="carousel-title">Explore the Top Places</h2>
      <Slider {...settings}>
        {museumData.slice(0,9).map((item) => (
          <div className="carousel-card" key={item.id}>
            <img src={item.img} alt={item.name} />
            <h3>{item.name}</h3>
            
          </div>
        ))}
      </Slider>
      <div className="show-more-container">
        <button 
          className="show-more-btn"
          onClick={()=>navigate("/museum")}
        >
          View All
        </button>
      </div>
    </div>
    
  );
};

export default OwlCarousel;