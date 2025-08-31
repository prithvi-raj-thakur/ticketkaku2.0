import React from 'react'
import HeroSection from '../components/HeroSection.jsx'
import ContactSection from '../components/ContactSection.jsx'
import Developers from '../components/Developers.jsx'
import Feedback from '../components/Feedback.jsx'
import Faq from '../components/Faq.jsx'
import AboutUs from '../components/Aboutus.jsx'
import OwlCarousel from '../components/OwlCarousel.jsx'
import Programs from '../components/Programs.jsx'

const Home = () => {
  return (
  <>
    <HeroSection/>
    <AboutUs/>
    <Programs/>
    <OwlCarousel/>
    <Faq/>
    <Feedback/>
    <Developers/>
    <ContactSection/>
  </>
  )
}

export default Home