import React from 'react'
import '../css files/Programs.css'
import program_1 from '../assets/program1.jpg'
import program_2 from '../assets/program2.jpg'
import program_3 from '../assets/program3.jpg'
import pi_1 from '../assets/park-i.svg'
import pi_2 from '../assets/hwh-i.svg'
import pi_3 from '../assets/museum-i.svg'

const Programs = () => {
  return (
    <div className='programs-section'>
      
      <div className="programs-header">
        <h2 className="programs-title">Ready to Travel Smart with TicketKaku?</h2>
        <p className="programs-subtitle">
          Book Tickets for
        </p>
      </div>

    
      <div className='programs'>
        <div className="program">
          <img src={program_1} alt="" />
          <div className="caption">
            <img src={pi_1} alt="" />
            <p>Parks</p>
          </div>
        </div>
        <div className="program">
          <img src={program_2} alt="" />
          <div className="caption">
            <img src={pi_2} alt="" />
            <p>Historical Places</p>
          </div>
        </div>
        <div className="program">
          <img src={program_3} alt="" />
          <div className="caption">
            <img src={pi_3} alt="" />
            <p>Museums</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Programs