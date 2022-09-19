import React, { useState } from "react";
import AddModal from "../component/add-modal.jsx";
import CurrentMealModal from "../component/currentmeal-modal.jsx";
import MealCardModal from "../component/mealcard-modal.jsx";
import AddSearchModal from "../component/add-searchbar-modal.jsx";


const Account = () => {
  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  return (
    <div>
      <div className="pages">
        <h2>Account</h2>
      </div>
      <AddModal
      show={show}
      handleClose={handleClose} />
      <CurrentMealModal
      show={show}
      handleClose={handleClose} />
      <MealCardModal
      show={show}
      handleClose={handleClose} />
      <AddSearchModal
      show={show}
      handleClose={handleClose} />
    </div>
  );
};

export default Account;