import { React, useState, useEffect } from 'react'
import { useParams } from 'react-router-dom';
import Card from '../components/Moviecard/Moviecard';
import axios from 'axios';
import './medialist.css';
export const Medialist = () => {
    const [media, setMedia] = useState([])
    const { mediaType } = useParams();
    const mtype = mediaType === 'movies' ? 'movie' : 'tvshow';
    useEffect(() => {
       axios.get(
  "https://filmfusion-p4wa.onrender.com/api/all/"
).then(response => {
            const allItems = response.data;
            const filteredItems = allItems.filter(item => item.type === mtype)
            setMedia(filteredItems)
        })
    }, [mtype])
    return (
        <div className="medialist">
            <h1>{mediaType === 'movies' ? 'Movies' : 'TV Shows'}</h1>
            <div className="grid">
                {media.length === 0 ? (
                    <p>No {mtype}s available</p>
                ) : (
                    media.map(item => (
                        <Card key={item.tmdb_id} item={item} mediaType={mtype} />
                    ))
                )}
            </div>
        </div>
    )
}
