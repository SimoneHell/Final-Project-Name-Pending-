import React, {useState} from "react";
import Button from 'react-bootstrap/Button';
import AddModal from '../component/add-modal.jsx';

const Account = ()=>{
    const [openAddModal, setOpenAddModal] = useState(false);

    return (
        <div>
        <div className="pages">
            <h2>Account</h2>
        </div>
        
        <Button variant="primary" onClick={() =>{setOpenAddModal(true);}}>Click me</Button>{' '}
        {openAddModal && <AddModal/>}

     
        </div>
    );
};

export default Account;