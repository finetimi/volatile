import React, { PureComponent } from 'react';
import ReactDOM from 'react-dom';


class Main extends PureComponent {


	render(){
		return (
			<div>
				<p> Path to bundle </p>
			</div>
		)
	}
}

const wrapper = document.getElementById("main");
wrapper ? ReactDOM.render(<Main />, wrapper) : false;