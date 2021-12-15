import React, { useState, use } from "react";
import {render} from 'react-dom' 
import {ThemeProvider, CssBaseline} from '@material-ui/core'
import theme from '../theme'
import {BrowserRouter as Router, Route} from 'react-router-dom'
import Home from '../pages/dictionary/Home'
import Definition from '../pages/dictionary/Definition'
import Bookmarks from '../pages/dictionary/Bookmarks'


function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline/>
      <Router>
          <Route exact path="/" render={() => <Home />} />
          <Route exact path="/search/word" render={() => <Definition />} />
          <Route exact path=" /bookmarks" render={() => <Bookmarks />} />
      </Router>
    </ThemeProvider>
  );
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
