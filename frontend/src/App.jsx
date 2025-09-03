import {Toaster} from 'react-hot-toast'
import { Route, Routes, useLocation } from 'react-router-dom'
import Footer from './components/Footer.jsx'
import Home from './pages/Home.jsx'
import Navbar from './components/Navbar.jsx'
import Museum from './pages/Museum.jsx'
import MuseumDetails from './pages/MuseumDetails.jsx'
import MyBookings from './pages/MyBookings.jsx'
import Chatbot from './pages/Chatbot.jsx'
import HelpChat from './pages/HelpChat.jsx'


function App() {
  const isAdminRoute = useLocation().pathname.startsWith('/admin')
const chatRoute = useLocation().pathname.startsWith('/chatbot')
const helpRoute = useLocation().pathname.startsWith('/help')
const hide = isAdminRoute || chatRoute || helpRoute
  return (

    <>
      <Toaster/>
       {!hide && <Navbar />} 
    {/* for admin routes, we don't want to show the navbar */}
    <Routes>
    <Route path='/' element={<Home/>}/>
    <Route path = '/museum' element={<Museum/>}/>
    <Route path = '/museum/:id' element={<MuseumDetails/>}/>
    <Route path='/my-bookings' element={<MyBookings/>}/>
    <Route path ='/chatbot' element={<Chatbot/>}/>
    <Route path ='/help' element={<HelpChat/>}/>

    </Routes>
    {!hide && <Footer/>}
    </>
  )
}

export default App
