import React from 'react'
import '../css files/HeroSection.css'

const HeroSection = () => {
 return (
    <div className='hero'>
        <main>
        <section>
            <h3>Want to Explore Kolkata?</h3>
            <h1>
            DO COME & VISIT <span className="change_content"></span>{" "}
            <span style={{ marginTop: "-10px" }}></span>
            </h1>
            <p>
            Streets alive with culture and grace,
            <br />
            Every turn, a magical place.
            <br />
            Let TicketKaku lead the way,
            <br />
            And paint your perfect Kolkata day.
            </p>
            <p className='abc'>"Your one-stop destination for city adventures starts here!"</p>
            
            <button className='btn'>KNOW MORE ➙</button>
 </section>
        </main>
      <button className="floating-btn" onClick={() => alert("Button clicked!")}>
          BOOK NOW
        </button>
    </div>
  )

}

export default HeroSection