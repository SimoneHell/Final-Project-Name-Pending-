import React from 'react';
import Container from 'react-bootstrap/Container';
import '../../styles/calendar.css';
import DailyPlan from './dailyplan.jsx';

function Calendar () {
    return(
        <Container>
            <DailyPlan/>
            <DailyPlan/>
            <DailyPlan/>
            <DailyPlan/>
            <DailyPlan/>
            <DailyPlan/>
            <DailyPlan/>
        </Container>
    )
};

export default Calendar;