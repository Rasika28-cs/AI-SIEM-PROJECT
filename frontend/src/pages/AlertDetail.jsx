import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import DashboardLayout from "../layouts/DashboardLayout";
import API from "../services/api";

import "../styles/alertDetail.css";

function AlertDetail() {

    const { id } = useParams();

    const [alertData, setAlertData] = useState(null);

    const [status, setStatus] = useState("");

    useEffect(() => {

        API.get(`/alerts/api/${id}/`)

            .then(response => {

                setAlertData(response.data);

                setStatus(response.data.status);

            })

            .catch(console.log);

    }, [id]);



    function saveStatus() {

        API.post(

            `/alerts/api/${id}/status/`,

            {
                status: status
            }

        )

            .then(() => {

                setAlertData({
                    ...alertData,
                    status: status
                });

                alert("Status Updated Successfully");

            })

            .catch(console.log);

    }



    if (!alertData) {

        return (

            <DashboardLayout>

                <h2>Loading...</h2>

            </DashboardLayout>

        );

    }



    return (

        <DashboardLayout>

            <h2>Alert Details</h2>

            <div className="detail-card">

                <p><strong>Attack:</strong> {alertData.attack_type}</p>

                <p><strong>Severity:</strong> {alertData.severity}</p>

                <p><strong>Status:</strong> {alertData.status}</p>

                <p><strong>Agent:</strong> {alertData.agent}</p>

                <p><strong>Event:</strong> {alertData.event_type}</p>

                <p><strong>Source:</strong> {alertData.source}</p>

                <p><strong>Message:</strong> {alertData.message}</p>

                <p><strong>Created:</strong> {alertData.created_time}</p>

            </div>

            <h3>Update Status</h3>

            <div className="status-box">

                <select

                    value={status}

                    onChange={(e) => setStatus(e.target.value)}

                >

                    <option value="Open">Open</option>

                    <option value="Investigating">
                        Investigating
                    </option>

                    <option value="Resolved">
                        Resolved
                    </option>

                </select>

                <button

                    onClick={saveStatus}

                >

                    Save

                </button>

            </div>

        </DashboardLayout>

    );

}

export default AlertDetail;