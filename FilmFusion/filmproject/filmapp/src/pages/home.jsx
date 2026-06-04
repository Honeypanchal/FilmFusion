import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './home.css';
import Card from '../components/Moviecard/Moviecard';
import { useNavigate } from 'react-router-dom';

export const Home = () => {
  const [movies, setMovies] = useState([]);
  const [tvShows, setTvShows] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    axios.get(
  "https://filmfusion-p4wa.onrender.com/api/all/"
)
      .then(response => {
        const allItems = response.data;
        const movieItems = allItems.filter(item => item.type === 'movie').slice(0, 6);
        const tvShowItems = allItems.filter(item => item.type === 'tvshow').slice(0, 6);
        setMovies(movieItems);
        setTvShows(tvShowItems);
      })
      .catch(error => {
        console.error('Error fetching movies and TV shows:', error);
      });
  }, []);

  return (
    <div className="home">
      <div className="section-header">
        <h1>Movies</h1>
        <button onClick={() => navigate('/list/movies')}>View More</button>
      </div>
      <div className="grid">
        {movies.length === 0 ? <p>No movies available</p> : null}
        {movies.map(movie => (
          <Card key={movie.tmdb_id} item={movie} mediaType="movie" />
        ))}
      </div>

      <div className="section-header">
        <h1>TV Shows</h1>
        <button onClick={() => navigate('/list/tvshow')}>View More</button>
      </div>
      <div className="grid">
        {tvShows.length === 0 ? <p>No TV shows available</p> : null}
        {tvShows.map(tvShow => (
          <Card key={tvShow.tmdb_id} item={tvShow} mediaType="tvshow" />
        ))}
      </div>
    </div>
  );
};