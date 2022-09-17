import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import "../../styles/account.css";

import AddModal from "../component/add-modal.jsx";

const Account = () => {
  const [openAddModal, setOpenAddModal] = useState(false);

  return (
     <div>
      <div className="pages">
        <Card id="CardAccount">
          <Card.Header>
            Account
          </Card.Header>
          <Card.Text>
            Information 
          </Card.Text>
        </Card>
      </div> 
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