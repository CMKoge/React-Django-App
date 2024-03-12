import axios from 'axios';
import React from 'react';

class App extends React.Component {

  state = { details: [], }

  componentDidMount() {

    let data;

    axios.get('http://localhost:8000/').then(res => {
      data = res.data;
      this.setState({ details: data });
    }).catch(err => {
      console.error(err);
    })
  }

  render() {
    return (
      <div>
        <header> Data Generated from Django </header>
        <hr />
        {this.state.details.map((output, id) => (
          <div key={id}>
            <h3>{output.name}</h3>
            <p>{output.dept}</p>
            <hr />
          </div>
        ))}
      </div>
    );
  }

}

export default App;
