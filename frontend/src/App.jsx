import {Toaster} from 'react-hot-toast'
import { Route, Routes, useLocation } from 'react-router-dom'
import Footer from './components/Footer.jsx'
import Home from './pages/Home.jsx'
import Navbar from './components/Navbar.jsx'
import Museum from './pages/Museum.jsx'
import MuseumDetails from './pages/MuseumDetails.jsx'
import Mybookings from './pages/Mybookings.jsx'
import Chatbot from './pages/Chatbot.jsx'
import Help from './pages/Help.jsx'


function App() {
  const isAdminRoute = useLocation().pathname.startsWith('/admin')

  return (

    <>
      <Toaster/>
       {!isAdminRoute && <Navbar />} 
    {/* for admin routes, we don't want to show the navbar */}
    <Routes>
    <Route path='/' element={<Home/>}/>
    <Route path = '/museum' element={<Museum/>}/>
    <Route path = '/museum/:id' element={<MuseumDetails/>}/>
    <Route path='/my-bookings' element={<Mybookings/>}/>
    <Route path ='/chatbot' element={<Chatbot/>}/>
    <Route path ='/help' element={<Help/>}/>

    </Routes>
    {!isAdminRoute && <Footer/>}
    </>
  )
}

export default App
