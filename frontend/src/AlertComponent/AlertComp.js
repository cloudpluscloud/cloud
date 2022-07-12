import React from "react"
import {Alert} from "react-bootstrap"
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCloud } from '@fortawesome/free-solid-svg-icons'

class AlertComp extends React.Component {
    componentDidMount = () => {
        console.log('component did mount');
        this.calculateSomething();
    }

    calculateSomething = () => {
        console.log('hello');
    }

    render = () => {
        return (
            <Alert variant="primary" style={{ width: "42rem" }}>
                <Alert.Heading>
                    Hello! Welcome to Cloud+!
                </Alert.Heading>
                <FontAwesomeIcon icon={faCloud} />
            </Alert>
        )
    }
}

export default AlertComp