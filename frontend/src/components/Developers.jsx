import React from "react";
import "../css files/Developers.css"; // Make sure your styles are correctly imported

const Developers = () => {
  return (
    <section className="developers-section">
      <h1 className="developers">Meet the Developers</h1>

      <div className="cards-container">

        <div className="card">
          <img src="../../images/prithvi.jpg" alt="Prithvi" className="avatar" />
          <h2>Prithvi Raj Thakur</h2>
          <div className="dsocial-icons">
            <a href="https://www.instagram.com/prithvi.fr/profilecard/?igsh=OGJ5eTNwczM3eTdh"><i className="fab fa-instagram"></i></a>
            <a href="#"><i className="fab fa-linkedin"></i></a>
            <a href="#"><i className="fab fa-github"></i></a>
          </div>
        </div>

        <div className="card">
          <img src="/images/sukhendu.jpg" alt="Sukhendu" className="avatar" />
          <h2>Sukhendu Chakraborty</h2>
          <div className="dsocial-icons">
            <a href="#"><i className="fab fa-instagram"></i></a>
            <a href="#"><i className="fab fa-linkedin"></i></a>
            <a href="#"><i className="fab fa-github"></i></a>
          </div>
        </div>

        <div className="card">
          <img src="/images/user.jpg" alt="Krishnendu" className="avatar" />
          <h2>Krishnendu Mandal</h2>
          <div className="dsocial-icons">
            <a href="#"><i className="fab fa-instagram"></i></a>
            <a href="#"><i className="fab fa-linkedin"></i></a>
            <a href="#"><i className="fab fa-github"></i></a>
          </div>
        </div>

        <div className="card">
          <img src="/images/user.jpg" alt="Sucharita" className="avatar" />
          <h2>Sucharita Das</h2>
          <div className="dsocial-icons">
            <a href="#"><i className="fab fa-instagram"></i></a>
            <a href="#"><i className="fab fa-linkedin"></i></a>
            <a href="#"><i className="fab fa-github"></i></a>
          </div>
        </div>

      </div>
    </section>
  );
};

export default Developers;