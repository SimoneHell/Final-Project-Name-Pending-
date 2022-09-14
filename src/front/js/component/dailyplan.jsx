import React from 'react';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import '../../styles/calendar.css';
import Stack from 'react-bootstrap/Stack';

function DailyPlan () {
    return(
            <Col>
            <Stack gap={4}>
                <div class="row" className='dayHeader'>Header</div>
                <div class="row-sm ms auto" className='meal'>Meal</div>
                <div class="row-sm ms auto" className='meal'>Meal</div>
                <div class="row-sm ms auto" className='meal'>Meal</div>
            </Stack>
            </Col>
         
    )
};

export default DailyPlan;