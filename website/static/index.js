$(function() {
    $('#sendBtn').bind('click', function() {
        let value = document.getElementById("msg").value;
        $.getJSON('/send_message',
        {val: value},
        (data) =>  {

        });
    });
});

function validate(name) {
    if (name.length >= 2){
        return true;
    }
    return false;
};



function update(){
    fetch('/get_messages')
        .then(function (response) {
            //return response.text();
            return response.json();
        }).then(function (json) {
            data = json['messages'];
            if (data.length > 0)
                document.querySelector("#test").textContent = data;
                console.log(data);
        });
    return false;
}