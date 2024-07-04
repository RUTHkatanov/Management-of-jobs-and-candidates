import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import RegisterUser from './components/RegisterUser';
import UploadResume from './components/UploadResume';
import NewJob from './components/NewJob';
import ViewJobs from './components/ViewJobs';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/register" component={RegisterUser} />
        <Route path="/upload-resume" component={UploadResume} />
        <Route path="/new-job" component={NewJob} />
        <Route path="/view-jobs" component={ViewJobs} />
      </Switch>
    </Router>
  );
};

export default App;
