
import { useParams, useNavigate } from "react-router-dom";
import {museumData} from "../assets/assets.js";
import "../css files/MuseumDetails.css";

const MuseumDetails = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const item = museumData.find((m) => m.id === id);

  if (!item) return <p>Item not found</p>;

  // Google Maps link using the name of the place
  const mapsLink =` https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(item.name)}`;

  return (
    <div className="details-container">
      <button onClick={() => navigate(-1)}>← Back</button>
      <img src={item.image} alt={item.name} />
      <h1>{item.name}</h1>
      <p>{item.longDescription}</p>

      <p><strong>Price:</strong> {Array.isArray(item.price) ? item.price.join(", ") : item.price}</p>
      <p><strong>Opening Time:</strong> {item.openingTime}</p>
      <p><strong>Closing Time:</strong> {item.closingTime}</p>
      <p><strong>Day Off:</strong> {item.dayoff}</p>
      <p><strong>Location:</strong> {item.location} &nbsp;|&nbsp; 
        <a href={mapsLink} target="_blank" rel="noopener noreferrer">View on Google Maps</a>
      </p>
    </div>
  );
};

export default MuseumDetails;