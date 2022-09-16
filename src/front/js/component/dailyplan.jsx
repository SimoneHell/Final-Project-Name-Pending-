import React, {useState} from 'react';
import Col from 'react-bootstrap/Col';
import '../../styles/calendar.css';
import Stack from 'react-bootstrap/Stack';
import DailyMeal from './meal-calendar.jsx';
import DayOfWeek from './day-week.jsx';

function DailyPlan () {
    return(
            <Col>
            <Stack gap={4}>
                <DayOfWeek/>
                <DailyMeal/>
                <DailyMeal/>
                <DailyMeal/>
            </Stack>
            </Col>
         
    )
};

export default DailyPlan;