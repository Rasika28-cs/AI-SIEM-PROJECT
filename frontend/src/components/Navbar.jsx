import "./../styles/navbar.css";

function Navbar() {
  return (
    <nav className="navbar">
      <div>
        <h2>AI SIEM Assistant</h2>
      </div>

      <div className="navbar-right">
        <span>Welcome, Admin</span>
      </div>
    </nav>
  );
}

export default Navbar;

function logout() {

    API.post("/accounts/logout/api/")

        .then(() => {

            window.location = "/";

        });

}