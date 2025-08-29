import React from 'react'
import HeroSection from '../components/HeroSection.jsx'
import ContactSection from '../components/ContactSection.jsx'
import Developers from '../components/Developers.jsx'
import Feedback from '../components/Feedback.jsx'
import Faq from '../components/Faq.jsx'

const Home = () => {
  return (
  <>
    <HeroSection/>
    <Faq/>
    <Feedback/>
    <Developers/>
    <ContactSection/>
  </>
  )
}

export default Home