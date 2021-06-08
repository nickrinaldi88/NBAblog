// Load main page onto this page

import React, { Component } from "react";
import Login from "./Login";
import CreateUser from "./CreateUser";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/">
            <p>This is the homepage</p>
          </Route>
          <Route path="/login" component={Login} />
          <Route path="/createuser" component={CreateUser} />
        </Switch>
      </Router>
    );
  }
}

// cmd: npm run dev
