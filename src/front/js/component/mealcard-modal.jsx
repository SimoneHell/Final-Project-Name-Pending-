import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import Card from 'react-bootstrap/Card';
import {FaHeart} from 'react-icons/fa';

export function MealCardModal() {
  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  return (
        <>
      <Button variant="primary" onClick={handleShow}>
        Meal Card Modal
      </Button>
    
      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
        </Modal.Header>
        <Modal.Body>
        <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="https://via.placeholder.com/286x180"/>
      <Card.Body>
        <Card.Title>Food Name</Card.Title>
        <Card.Text>
         API data here 
        </Card.Text>
      </Card.Body>
    </Card>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="primary" onClick={handleClose}>
            Add
          </Button>
          <Button variant="primary" onClick={handleClose}>
            <FaHeart/>
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}

export default MealCardModal;
