import React from 'react';
import '../index.css';
import '../css files/Footer.css' // assuming index.css is your global style


function Footer() {
  
  return (
    <footer className="footer">
      <div className="footer-top">
        <h2>Ready to Travel Smart with TicketKaku?</h2>
        <p>Join thousands who’ve simplified their bookings with our AI-powered chatbot.</p>

 <button  onClick={()=>{scrollTo(0, 0); }} className="signup-btn">Sign Up Now</button>

       
      </div>

      <div className="footer-main">
        <div className="footer-section brand">
          <h3 className="brand-name">🎫 TicketKaku</h3>
          <p>Your intelligent companion for seamless ticket booking and travel planning in Kolkata.</p>
          <div className="social-icons">
            <i className="fa-brands fa-facebook-f"></i>
            <i className="fa-brands fa-x-twitter"></i>
            <i className="fa-brands fa-instagram"></i>
            <i className="fa-brands fa-linkedin-in"></i>
          </div>
        </div>

        <div className="footer-section links">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">Book Tickets</a></li>
            <li><a href="#">About Us</a></li>
            <li><a href="#">Feedback</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </div>

        <div className="footer-section features">
          <h4>Our Features</h4>
          <ul>
            <li>Instant Booking</li>
            <li>AI Chatbot Assistance</li>
            <li>QR Code Tickets</li>
            <li>Secure Payments</li>
            <li>Booking History</li>
          </ul>
        </div>

        <div className="footer-section contact">
          <h4>Contact Us</h4>
          <p>📍 123, Travel Street, Kolkata, 700152</p>
          <p>📞 +91 7462 936 291</p>
          <p>📧 support@ticketkaku.com</p>
        </div>
      </div>

      <div className="footer-bottom">
        <p>© 2025 Algo Rhythm. All rights reserved.</p>
        <div className="footer-links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Service</a>
          <a href="#">FAQ's</a>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
