import React from "react";
import PropTypes from "prop-types";


const Input = ({ label, text, type, id, value, handleChange}) =>(
	<div className="form-group">
		<label htmlFor={label}>
			{text}
		</label>
	</div>
);

export default Input;