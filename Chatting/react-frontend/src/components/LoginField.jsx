import { useState, useRef } from "react";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import { getCSRFToken } from "./auth";

function LoginField() {
    const navigate = useNavigate();

    // State for input values
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    // Refs for input fields and wrong message
    const usernameInputRef = useRef(null);
    const passwordInputRef = useRef(null);
    const wrongMessageRef = useRef(null);

    const login = () => {
        fetch("http://127.0.0.1:8000/login/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken()
            },
            credentials: 'include',
            body: JSON.stringify({ username: username, password: password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Hide error and reset styles
                wrongMessageRef.current.style.visibility = "hidden";
                usernameInputRef.current.style.backgroundColor = "#949ca9";
                passwordInputRef.current.style.backgroundColor = "#949ca9";
                usernameInputRef.current.style.borderColor = "ffffff00";
                navigate('/register');
            } else {
                // Show error and update styles
                wrongMessageRef.current.style.visibility = "visible";
                usernameInputRef.current.style.backgroundColor = "#f8d7da";
                passwordInputRef.current.style.backgroundColor = "#f8d7da";
                usernameInputRef.current.style.borderColor = "#fc0303";
                passwordInputRef.current.style.borderColor = "#fc0303";
            }
        })
        .catch(error => console.error("Error:", error));
    };

    return(
        <div className="login-popup">
            <h2 className="welcome-text">Welcome back!</h2>

            <div className="input-group">
                <label htmlFor="username" className="login-label"><b>Username</b></label>
                <br></br>
                <input
                    type="text"
                    name="username"
                    id="username-input"
                    ref={usernameInputRef}
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
            </div>

            <div className="input-group">
                <label htmlFor="password" className="login-label"><b>Password</b></label>
                <br></br>
                <input
                    type="password"
                    name="password"
                    id="password-input"
                    ref={passwordInputRef}
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <br></br>
                <button className="login-button" onClick={login}>Login</button>
            </div>

            <b id="wrong-text" ref={wrongMessageRef}>Wrong Username or Password*</b>
            <p className="newacc-link">New User? <Link to={"/register"}>Create account</Link></p>
        </div>
    );
}

export default LoginField;
