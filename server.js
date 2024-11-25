const axios = require('axios');

// 获取所有学生
axios.get('http://127.0.0.1:5000/students')
    .then(response => {
        if (response.data.length === 0) {
            console.log('No students found.');
        } else {
            console.log('All students:', response.data);
        }
    })
    .catch(error => {
        console.error('Error fetching students:', error);
    });