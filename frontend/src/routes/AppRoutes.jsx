import { BrowserRouter, Routes, Route } from "react-router-dom";

import Register from "../pages/Register";
import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import Logs from "../pages/Logs";
import Alerts from "../pages/Alerts";
import AlertDetail from "../pages/AlertDetail";
import Agents from "../pages/Agents";
import NotFound from "../pages/NotFound";
import ProtectedRoute from "../components/ProtectedRoute";

function AppRoutes() {

    return (

        <BrowserRouter>

            <Routes>

                <Route
                    path="/"
                    element={<Login />}
                />

                <Route
                    path="/register"
                    element={<Register />}
                />

                <Route
                    path="/dashboard"
                    element={
                        <ProtectedRoute>
                            <Dashboard />
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="/logs"
                    element={
                        <ProtectedRoute>
                            <Logs />
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="/alerts"
                    element={
                        <ProtectedRoute>
                            <Alerts />
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="/alerts/:id"
                    element={
                        <ProtectedRoute>
                            <AlertDetail />
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="/agents"
                    element={
                        <ProtectedRoute>
                            <Agents />
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="*"
                    element={<NotFound />}
                />

            </Routes>

        </BrowserRouter>

    );

}

export default AppRoutes;