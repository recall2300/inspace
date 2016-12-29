import React from "react"

import {connect} from "react-redux"

import * as counterActions from "../actions/counterActions"
import Headline from "../components/Headline"

@connect(state => ({
    counters: state.counters,
}))
export default class SampleAppContainer extends React.Component {
    handleClick() {
        let {dispatch} = this.props;
        dispatch(counterActions.increaseCounter())
    }

    render() {
        let {counters} = this.props
        return (
            <div className="container">
                <div className="row">
                    <div className="col-sm-12">
                        <Headline>Sample App!</Headline>
                        <div onClick={() => this.handleClick()}>INCREASE</div>
                        <p>{counters.clicks}</p>
                        <p>{process.env.BASE_API_URL}</p>
                    </div>
                </div>
            </div>
        )
    }
}