function inputChanged(event) {
    if (event.key === 'Enter') {
        fetch('/gues?n=' + event.target.value)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                document.getElementById("result").value = data["result"];
                document.getElementById("numberInput").value = '';
            });
    }
}

function buttonClicked() {
    fetch('/change')
}





