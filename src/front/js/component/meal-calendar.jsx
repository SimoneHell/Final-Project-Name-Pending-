import React, {useState} from 'react';
import '../../styles/calendar.css';
import {FaPlus} from "react-icons/fa";

function DailyMeal () {
    const [isSelected, setIsSelected] = useState(false);
    const pickMeal = () => setIsSelected(!isSelected);
  
    return(
        <div class="row-sm ms auto" className='meal' activeclassname="active" >
            <FaPlus onClick={pickMeal}/>
            </div>
    )
};

export default DailyMeal;