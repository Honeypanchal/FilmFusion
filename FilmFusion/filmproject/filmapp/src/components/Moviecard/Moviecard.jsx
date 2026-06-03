import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Moviecard.css';

const Card = ({ item, mediaType }) => {
    const navigate = useNavigate();

    const handleClick = () => {
        navigate(`/${mediaType}/${item.tmdb_id}`);
    };

    return (
        <div className="card" onClick={handleClick}>
            <img src={item.poster_path_w500} alt={item.title || item.name} />
            <div className="card-info">
                <p>{item.title || item.name}</p>
            </div>
        </div>
    );
};

export default Card;
