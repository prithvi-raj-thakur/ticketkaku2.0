import React, { useRef } from 'react';
import { FaFacebookF, FaInstagram, FaLinkedinIn } from 'react-icons/fa';
import { FaXTwitter } from 'react-icons/fa6';
import emailjs from 'emailjs-com';
import '../css files/ContactSection.css';

const ContactSection = () => {
  const formRef = useRef();

  const handleSubmit = (e) => {
    e.preventDefault();

    emailjs.sendForm(
      "service_1gay4ba",      // from EmailJS dashboard
      "YOUR_TEMPLATE_ID",     // from EmailJS dashboard
      formRef.current,
      "HWKWPsqlfKt-3owdi"       // from EmailJS account
    )
    .then(
      (result) => {
        console.log(result.text);
        alert("✅ Message sent successfully!");
        formRef.current.reset();
      },
      (error) => {
        console.error(error.text);
        alert("❌ Failed to send message. Try again.");
      }
    );
  };

  return (
    <section id="contact" className="contact-section">
      <h2>Contact Us</h2>
      <p>
        Have questions about Ticketkaku? We're here to help you optimize your travelling practices with our technology.
      </p>

      <div className="contact-container">
        {/* Left Info Section */}
        <div className="contact-info">
          <h3>Get in Touch</h3>
          <div className="info-box">
            <p>
              <strong>📞 Phone</strong><br />
              +91 7462 936 291<br />
              +91 1800 2345 6789 (Toll Free)
            </p>
            <p>
              <strong>📧 Email</strong><br />
              info@TicketKaku.com<br />
              support@TicketKaku.com
            </p>
            <p>
              <strong>📍 Address</strong><br />
              123 Explore Agency, Travel Street<br />
              Kolkata, 700152<br />
              India
            </p>
          </div>

          <div className="csocial-icons">
            <a href="#"><FaFacebookF /></a>
            <a href="#"><FaXTwitter /></a>
            <a href="#"><FaInstagram /></a>
            <a href="#"><FaLinkedinIn /></a>
          </div>
        </div>

        {/* Right Contact Form */}
        <div className="contact-form">
          <h3>Send Us a Message</h3>
          <form ref={formRef} onSubmit={handleSubmit}>
            <div className="input-row">
              <input type="text" name="user_name" placeholder="e.g. Elon Musk" required />
              <input type="email" name="user_email" placeholder="e.g. elon@example.com" required />
            </div>
            <div className="input-row">
              <input type="tel" name="user_phone" placeholder="e.g. +91 7462936291" required />
              <select name="subject" required>
                <option value="">Select a subject</option>
                <option value="support">Support</option>
                <option value="inquiry">General Inquiry</option>
                <option value="feedback">Feedback</option>
              </select>
            </div>
            <textarea name="message" rows="5" placeholder="Enter your message here..." required></textarea>
            <button id="submit" type="submit">📨 Send Message</button>
          </form>
        </div>
      </div>
    </section>
  );
};

export default ContactSection;