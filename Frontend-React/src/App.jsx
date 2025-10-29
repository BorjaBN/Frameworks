import { useState } from 'react'
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import './App.css'
import HomePage from './pages/HomePage'
import MoviesPage from './pages/MoviesPage'
import AboutPage from './pages/AboutPage'
import ContactPage from './pages/ContactPage'
import MovieDetailPage from './pages/MovieDetailPage'
import NotFoundPage from './pages/NotFoundPage'

function App() {
 
  return (
    <>
    <Router>
      <Routes>
        <Route path= "/" element={<HomePage />}/>
        <Route path= "/movies" element={<MoviesPage />}/>
        <Route path= "/about" element={<AboutPage />}/>
        <Route path= "/contact" element={<ContactPage />}/>

        <Route path= "/movies/:id" element={<MovieDetailPage />}/>

        <Route path= "*" element={<NotFoundPage />}/>


      </Routes>
    </Router>
    </>
  )
}

export default App
