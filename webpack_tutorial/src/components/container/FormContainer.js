import React, { Component } from "react";
import ReactDOM from "react-dom";
import Input from "../presentational/Input";


class FormContainer extends PureComponent{

	constructor(){
		super();
		this.state = {
			title: ""
		};

		this.handleChange = this.handleChange.bind(this);	
	}

	handleChange(event){
	}

	render(){
		return (
			<form id="article-form">
				<Input 
					text="SEO Title"
					label="seo_title"
					type="text"
					value="seo_title"
					handleChange={this.handleChange}
				/>
				Built Form
			</form>
		)
	}

}

export default FormContainer;