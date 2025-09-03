import React, { useState } from "react";
import "../css files/MyBookings.css";
import { FaUser } from "react-icons/fa";

const MyBookings = () => {
  const [activeTab, setActiveTab] = useState("upcoming");

  const bookings = [
    {
      place: "Science City",
      ticket_id: "xxxxxx",
      date: "xx-xx-xxxx",
      fare: 150,
      persons: 4,
      status: "completed",
    },
    {
      place: "Victoria Memorial",
      ticket_id: "xxxxxx",
      date: "xx-xx-xxxx",
      fare: 150,
      persons: 2,
      status: "upcoming",
    },
  ];

  return (
    <div className="container">
      <h2 className="heading">My Bookings</h2>

      {/* Tabs */}
      <div className="tabs">
        <button
          className={`tab ${activeTab === "upcoming" ? "active" : ""}`}
          onClick={() => setActiveTab("upcoming")}
        >
          Upcoming
        </button>
        <button
          className={`tab ${activeTab === "completed" ? "active" : ""}`}
          onClick={() => setActiveTab("completed")}
        >
          Completed
        </button>
      </div>

      {/* Tab Contents */}
      <div className="tab-content">
        {bookings
          .filter((b) => b.status === activeTab)
          .map((booking, index) => (
            <div key={index} className="card">
              <div className="card-header">
                <h4>{booking.place}</h4>
                <div className="person-count">
                  <FaUser /> {booking.persons}
                </div>
              </div>

              <div className="card-row">
                <span>Ticket ID: {booking.ticket_id}</span>
                <span>Date: {booking.date}</span>
              </div>

              <div className="card-row">
                <span>Fare: ₹{booking.fare}</span>
              </div>
            </div>
          ))}
      </div>
    </div>
  );
};

export default MyBookings;