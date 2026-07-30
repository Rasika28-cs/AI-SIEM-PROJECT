import { useState } from "react";
import { useNavigate } from "react-router-dom";

import API from "../services/api";

import "../styles/login.css";

function Login() {

    const navigate = useNavigate();

    const [username, setUsername] = useState("");

    const [password, setPassword] = useState("");

    const [error, setError] = useState("");

    function login(e) {

        e.preventDefault();

        API.post("/login/api/", {
            username,
            password
        })

        .then((response) => {

            console.log(response.data);

            sessionStorage.setItem("loggedIn", "true");

            navigate("/dashboard");

        })

        .catch((error) => {

            console.log(error.response?.data);

            setError("Invalid username or password");

        });

    }

    return (

        <div className="login-page">

            <form
                className="login-box"
                onSubmit={login}
            >

                <h2>AI SIEM Login</h2>

                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <button>

                    Login

                </button>

                <p className="error">

                    {error}

                </p>

            </form>

        </div>

    );

}

export default Login;