
import { Link, useNavigate } from 'react-router-dom'

import logo from "../assets/logo.svg"
import { SignUpButton, useClerk, UserButton, useUser } from '@clerk/clerk-react'
import '../css files/Navbar.css'
import { useEffect,useState } from 'react'
import logoWhite from '../assets/ticketkaku_white.svg'
import logoBlack from '../assets/ticketkaku_black.svg'

const Navbar = () => {
  const [scrolled, setScrolled] = useState(false);

const {user} = useUser() 
const {openSignIn} = useClerk()
const navigate = useNavigate()

useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50) // scroll threshold
    }
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])


  return (
  <nav className={`navbar ${scrolled ? 'scrolled' : ''}`}>
      {/* show logo depending on scroll */}
      <img
        src={scrolled ? logoBlack : logoWhite}
        alt="TicketKaku Logo"
        className="logo"
      />
        <ul>
            <li> <Link onClick={()=>{scrollTo(0, 0)}} to="/">Home</Link></li>
            <li><Link onClick={()=>{window.scrollTo(0,0); }} to="/#owl">Museums</Link></li>
            <li><Link onClick={()=>{scrollTo(0, 0);}} to="/my-bookings">My Bookings</Link></li>
            <li><Link onClick={()=>{window.scrollTo(0, 0); }} to="/#aboutus">About Us</Link></li>
            <li><Link onClick={()=>{scrollTo(0, 0);}} to="/help">Help</Link></li>
            {
              !user? (<SignUpButton><li><button onClick={openSignIn} className='btn'>LOGIN</button></li></SignUpButton>):
              (
                 <UserButton>
           <UserButton.MenuItems>
            
             
           </UserButton.MenuItems>
            </UserButton>
              )
            }
           
        </ul>
    </nav>
  )
}


export default Navbar