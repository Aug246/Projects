import { Link } from "react-router-dom" 

function LoginField() {
    return(
        <div className="login-popup">
            <div className="input-group">
                <label for="name" className="login-label"> <b>First Name</b> </label>
                <br></br>
                <input type="text" name="name" className="firstname-input"></input>
            </div>

            <div className="input-group">
                <label for="lastname" className="login-label"> <b>First Name</b> </label>
                <br></br>
                <input type="text" name="lastname" className="lastname-input"></input>
            </div>

            <div className="input-group">
                <label for="username" className="login-label"> <b>Username</b> </label>
                <br></br>
                <input type="text" name="username" className="username-input"></input>
            </div>

            <div className="input-group">
                <label for="password" className="login-label"> <b>Password</b> </label>
                <br></br>
                <input type="text" name="password" className="password-input"></input>
                <br></br>
                <button className="login-button">Create Account</button>
            </div>

        </div>
    );
}  

export default LoginField