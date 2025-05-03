document.getElementById('submit-resume').addEventListener('click', function() {
    const fileInput = document.getElementById('resume-upload');
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    fetch('http://127.0.0.1:5444/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('suggestions-list').innerHTML = 
            `<p>File uploaded successfully: ${data.filename}</p>`;
    })
    .catch(error => console.error('Error:', error));
});
