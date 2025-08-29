
import { Link, useNavigate } from 'react-router-dom'

import logo from "../assets/logo.svg"
import { SignUpButton, useClerk, UserButton, useUser } from '@clerk/clerk-react'
import '../css files/Navbar.css'

const Navbar = () => {


const {user} = useUser() 
const {openSignIn} = useClerk()
const navigate = useNavigate()


  return (
    <nav className='container'>
        <img src={logo} alt="" className='logo' />
        <ul>
            <li> <Link onClick={()=>{scrollTo(0, 0)}} to="/">Home</Link></li>
            <li><Link onClick={()=>{scrollTo(0, 0); }} to="/">Museums</Link></li>
            <li><Link onClick={()=>{scrollTo(0, 0);}} to="/my-bookings">My Bookings</Link></li>
            <li><Link onClick={()=>{scrollTo(0, 0); }} to="/">About Us</Link></li>
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