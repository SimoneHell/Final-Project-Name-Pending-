import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import CurrentMealCard from './Currentmeal-card.jsx';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import SearchBar from './searchbar.jsx';
import '../../styles/addsearchmodal.css'

export function AddSearchModal() {
  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
/*Tried to custom size modal with 
contentClassName='modal-height' 
dialogClassName='modal-width' 
but it didn't work. To find another solution */
  return (
        <>
      <Button variant="primary" onClick={handleShow}>
        Add Search Modal
      </Button>
  
      <Modal size="lg" show={show} onHide={handleClose} > 
        <Modal.Header closeButton>
        </Modal.Header>
        <Modal.Body className='show-grid'>
          <Container fluid>
            <Row>
              <Col md={4}>
                <CurrentMealCard/>
                <Button variant="primary" onClick={handleClose}>
                  Delete
                </Button>
                <Button variant="primary" onClick={handleClose}>
                  Next
                </Button>
                <Button variant="primary" onClick={handleClose}>
                  Back
                </Button>
              </Col>
              <Col md={8}>
                <SearchBar/>
              </Col>
            </Row>
          </Container>
            
        </Modal.Body>
          
      </Modal>
    </>
  );
}

export default AddSearchModal;