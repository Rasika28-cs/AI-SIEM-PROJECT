import { useEffect, useState } from "react";

import DashboardLayout from "../layouts/DashboardLayout";
import API from "../services/api";

import "../styles/dashboard.css";


function Dashboard() {


    const [data, setData] = useState(null);


    useEffect(() => {

        API.get("/dashboard/api/")
        .then(response => {

            setData(response.data);

        })
        .catch(error => {

            console.log(error);

        });


    }, []);



    if (!data) {

        return (

            <DashboardLayout>

                <h2>
                    Loading Dashboard...
                </h2>

            </DashboardLayout>

        );

    }



    return (

        <DashboardLayout>


            <h2>
                AI SIEM Dashboard
            </h2>


            <p>
                Welcome, Admin
            </p>



            <div className="cards">


                <div className="card">

                    <h3>Total Logs</h3>

                    <h1>
                        {data.total_logs}
                    </h1>

                </div>



                <div className="card">

                    <h3>Total Alerts</h3>

                    <h1>
                        {data.total_alerts}
                    </h1>

                </div>



                <div className="card">

                    <h3>Online Agents</h3>

                    <h1>
                        {data.online_agents}
                    </h1>

                </div>



                <div className="card">

                    <h3>High Alerts</h3>

                    <h1 className="danger">

                        {data.high_alerts}

                    </h1>

                </div>


            </div>



            <h3>
                Recent Alerts
            </h3>


            <table>


                <thead>

                    <tr>

                        <th>
                            Attack
                        </th>

                        <th>
                            Severity
                        </th>

                        <th>
                            Status
                        </th>

                        <th>
                            Time
                        </th>


                    </tr>

                </thead>


                <tbody>


                {
                    data.recent_alerts.map(
                        (alert,index)=>(

                        <tr key={index}>

                            <td>
                                {alert.attack_type}
                            </td>

                            <td>
                                {alert.severity}
                            </td>

                            <td>
                                {alert.status}
                            </td>

                            <td>
                                {alert.created_time}
                            </td>


                        </tr>

                        )
                    )
                }


                </tbody>


            </table>



            <h3>
                Recent Security Logs
            </h3>


            <table>


                <thead>

                    <tr>

                        <th>
                            Time
                        </th>

                        <th>
                            Agent
                        </th>

                        <th>
                            Event
                        </th>

                        <th>
                            Severity
                        </th>


                    </tr>

                </thead>


                <tbody>


                {
                    data.recent_logs.map(
                        (log,index)=>(

                        <tr key={index}>

                            <td>
                                {log.timestamp}
                            </td>

                            <td>
                                {log.agent__hostname}
                            </td>

                            <td>
                                {log.event_type}
                            </td>

                            <td>
                                {log.severity}
                            </td>


                        </tr>

                        )
                    )
                }


                </tbody>


            </table>



        </DashboardLayout>

    );

}


export default Dashboard;