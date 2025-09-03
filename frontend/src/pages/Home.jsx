import{useRef,useEffect} from 'react'
import HeroSection from '../components/HeroSection.jsx'
import ContactSection from '../components/ContactSection.jsx'
import Developers from '../components/Developers.jsx'
import Feedback from '../components/Feedback.jsx'
import Faq from '../components/Faq.jsx'
import AboutUs from '../components/Aboutus.jsx'
import OwlCarousel from '../components/OwlCarousel.jsx'
import Programs from '../components/Programs.jsx'
import { useLocation } from 'react-router-dom'
const Home = () => {
  const museumRef = useRef(null);
  const aboutRef = useRef(null);
  const location = useLocation();

   useEffect(() => {
    if (location.hash === '#owl') {
      museumRef.current?.scrollIntoView({ behavior: 'smooth' });
       window.history.replaceState(null, '', '/');
    } else if (location.hash === '#aboutus') {
      aboutRef.current?.scrollIntoView({ behavior: 'smooth' });
       window.history.replaceState(null, '', '/');
    }
  }, [location]);
  
  return (
  <>
    <HeroSection/>
     <div ref={museumRef} id="aboutus">
        <AboutUs />
      </div>
    <Programs/>
    <div ref={museumRef} id="owl">
        <OwlCarousel/>
      </div>
    <Faq/>
    <Feedback/>
    <Developers/>
    <ContactSection/>
  </>
  )
}

export default Home