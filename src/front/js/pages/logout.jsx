import React, {useState} from "react";
import Button from 'react-bootstrap/Button';
import LogoutModal from '../component/logout-modal.jsx';

const Logout = ()=>{
    const [openLogoutModal, setOpenLogoutModal] = useState(false);

    return (
        <div>
        <div className="pages">
            <h2>Log out</h2>
        </div>
        
        <Button variant="primary" onClick={() =>{setOpenLogoutModal(true);}}>Click me</Button>{' '}
        {openLogoutModal && <LogoutModal/>}

     
        </div>
    );
};

export default Logout;