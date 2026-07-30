import { Link } from "react-router-dom";

import "../styles/notfound.css";

function NotFound() {

    return (

        <div className="notfound">

            <h1>404</h1>

            <h2>Page Not Found</h2>

            <p>

                Sorry, the page you are looking for doesn't exist.

            </p>

            <Link to="/dashboard">

                Go to Dashboard

            </Link>

        </div>

    );

}

export default NotFound;