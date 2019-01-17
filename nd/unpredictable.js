const fs = require('fs');
const cache = {};
const

function inconsistentFileRead(filename, callback){
	if (cache[filename]){
		return callback(cache[filename]);
	}
	else {
		fs.readFile(filename, 'utf8', (err, data)=>{
			cache[filename] = data;
			callback(data); 
		})
	}
}

