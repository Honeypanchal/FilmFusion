import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './details.css';

export const Details = () => {
    const { mediaType, id } = useParams();
    console.log(mediaType)
    const [item, setItem] = useState(null);

    useEffect(() => {
        axios.get('http://localhost:8000/api/all/')
            .then(response => {
                const allItems = response.data;
                console.log('ok')
                console.log(allItems)
                const foundItem = allItems.find(
                    i => i.type === mediaType && i.tmdb_id.toString() === id
                );

                setItem(foundItem);
            })
            .catch(error => {
                console.error('Error fetching item details:', error);
            });
    }, [mediaType, id]);

    if (!item) {
        return <div>Loading...</div>;
    }

    return (
        <div className="details" style={{ backgroundImage: `url(${item.backdrop_path_original})` }}>
            <div className="details-content">
                <img src={item.poster_path_original} alt={item.title || item.name} className="details-poster" />
                <div className="details-info">
                    <h1>{item.title || item.name}</h1>
                    <p>{item.description}</p>
                    <button className="watch-trailer-btn" onClick={() => window.open(item.trailer_url, "_blank")}>
                        Watch Trailer
                    </button>
                    <button className="watch-now-btn">
                        Watch Now
                    </button>
                </div>
            </div>
        </div>
    );
};
