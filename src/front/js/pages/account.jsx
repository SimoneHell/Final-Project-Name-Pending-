import React, { useContext, useState } from "react";
import { useEffect } from "react";
import "../../styles/account.css";
import getState from "../store/flux";
import AddModal from "../component/add-modal.jsx";
import {
  Container,
  Form,
  InputGroup,
  Accordion,
  Card,
  Button,
} from "react-bootstrap";

const Account = () => {
  const [openAddModal, setOpenAddModal] = useState(false);

  return (
    <div className="pages">
      <Card id="CardAccount">
        <Card.Title id="CardTitle"> Account Settings </Card.Title>
        <Card.Body>
          <Accordion defaultActiveKey={['0']} id="emailacc">
            <Accordion.Item eventKey="1">
              <Accordion.Header>Change Email</Accordion.Header>
              <Accordion.Body>
                <Form.Label htmlFor="basic-url">
                  Please enter your new Email
                </Form.Label>
                <InputGroup classname="mb-2">
                  <Form.Control
                    placeholder="Email"
                    aria-label="email"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <Form.Label htmlFor="basic-url">
                  Please confirm your new Email
                </Form.Label>
                <InputGroup classname="mb-2">
                  <Form.Control
                    placeholder=" Repeat Email"
                    aria-label="email"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <Button id="emailbtn"> Submit Changes</Button>
              </Accordion.Body>
            </Accordion.Item>
          </Accordion>

          <Accordion defaultActiveKey="0" id="passacc">
            <Accordion.Item eventKey="2">
              <Accordion.Header>Change Password</Accordion.Header>
              <Accordion.Body>
                <Form.Label htmlFor="basic-url">
                  Please enter your new Password
                </Form.Label>
                <InputGroup classname="mb-2">
                  <Form.Control
                    placeholder="Password"
                    aria-label="username"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <Form.Label htmlFor="basic-url">
                  Please confirm your new Password
                </Form.Label>
                <InputGroup classname="mb-2">
                  <Form.Control
                    placeholder="Repeat Password"
                    aria-label="username"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <Button id="passbtn"> Submit Changes</Button>
              </Accordion.Body>
            </Accordion.Item>
          </Accordion>
        </Card.Body>
      </Card>
    </div>
  );
};
export default Account;

/*  <Button
        variant="primary"
        onClick={() => {
          setOpenAddModal(true);
        }}
      >
        Click me
    </Button>{" "}
      {openAddModal && <AddModal />}
*/
