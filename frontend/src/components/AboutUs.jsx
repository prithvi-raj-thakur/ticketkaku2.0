import React from "react";
import "../css files/AboutUs.css";
import wbmapimage from '../assets/wb_map.jpg'

const AboutUs = () => {
  return (
    <section className="about-section">
      <div className="about-header">
        <h1>About Us</h1>
        <p className="subheading">
          Discover TicketKaku – Your AI-powered ticket booking assistant in Kolkata
        </p>
      </div>

      <div className="about-content">
        {/* Left Side Image */}
        <div className="about-image">
          <img src={wbmapimage} alt="About TicketKaku" />
        </div>

        {/* Right Side Text */}
        <div className="about-text">
          <p>
            TicketKaku is an AI-powered platform designed to make ticket booking
            simple, fast, and reliable. With our chatbot-based interface, you can
            seamlessly book tickets for museums, parks, and popular tourist
            attractions across Kolkata.
          </p>
          <p>
            Our mission is to provide a hassle-free experience where you can
            browse, book, and pay securely—all from one place. No more long
            queues or confusing processes—TicketKaku ensures your journey starts
            stress-free.
          </p>
          <p>
            With instant booking confirmations, QR-based digital tickets, and
            personalized suggestions, we bring you the future of smart tourism in
            Kolkata. TicketKaku is here to redefine how you explore the City of
            Joy!
          </p>
        </div>
      </div>
    </section>
  );
};

export default AboutUs;