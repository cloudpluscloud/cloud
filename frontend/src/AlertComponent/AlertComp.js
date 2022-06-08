import React from "react"
import {Alert} from "react-bootstrap"

class AlertComp extends React.Component {
    render() {
        return (
            <Alert variant="primary" style={{ width: "42rem" }}>
                <Alert.Heading>
                    Hello! Welcome to Cloud+!
                </Alert.Heading>
            </Alert>
        )
    }
}

export default AlertComp