import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";

import API from "../services/api";

import "../styles/register.css";

function Register() {

    const navigate = useNavigate();

    const [formData, setFormData] = useState({

        username: "",
        email: "",
        password1: "",
        password2: "",
        role: "Analyst"

    });

    const [error, setError] = useState("");

    function handleChange(e) {

        setFormData({

            ...formData,
            [e.target.name]: e.target.value

        });

    }

    function register(e) {

        e.preventDefault();

        API.post("/register/api/", formData)

            .then(() => {

                navigate("/dashboard");

            })

            .catch(error => {

                if (error.response?.data?.errors) {

                    setError(JSON.stringify(error.response.data.errors));

                }

                else {

                    setError("Registration Failed");

                }

            });

    }

    return (

        <div className="register-page">

            <form
                className="register-box"
                onSubmit={register}
            >

                <h2>AI SIEM Register</h2>

                <input
                    type="text"
                    name="username"
                    placeholder="Username"
                    value={formData.username}
                    onChange={handleChange}
                />

                <input
                    type="email"
                    name="email"
                    placeholder="Email"
                    value={formData.email}
                    onChange={handleChange}
                />

                <input
                    type="password"
                    name="password1"
                    placeholder="Password"
                    value={formData.password1}
                    onChange={handleChange}
                />

                <input
                    type="password"
                    name="password2"
                    placeholder="Confirm Password"
                    value={formData.password2}
                    onChange={handleChange}
                />

                <select
                    name="role"
                    value={formData.role}
                    onChange={handleChange}
                >

                    <option value="Admin">Admin</option>
                    <option value="Analyst">Analyst</option>
                    <option value="Viewer">Viewer</option>

                </select>

                <button>

                    Register

                </button>

                <p className="error">

                    {error}

                </p>

                <p>

                    Already have an account?

                    <Link to="/login">

                        Login

                    </Link>

                </p>

            </form>

        </div>

    );

}

export default Register;