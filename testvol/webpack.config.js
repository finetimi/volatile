const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');

module.exports = {
	entry: './src/index.js',
	module:{
		rules:[
			{
				test: /\.(js|jsx)/,
				exclude: /node_modules/,
				use: {
					loader: "babel-loader"
				}
			}
		]
	},
	plugins: [
		new HtmlWebpackPlugin({
			title: 'My Name',
			filename: 'index.html',
			template: './src/index.html'
		})
	]
}