var bindings = null;

function create_secret(message, secret) {
    if (bindings === null) {
        bindings = new Module.EmscriptenBindings();
    }
    return message + bindings.create_secret(secret);
}

function reveal_secret(message) {
    if (bindings === null) {
        bindings = new Module.EmscriptenBindings();
    }
    return bindings.extract_secret(message);
}

function create_secret_button_pressed() {
    var message = document.getElementById('id_message').value;
    var secret = document.getElementById('id_secret').value;
    var result = create_secret(message, secret);
    document.getElementById('id_secret_string').value = result;
    var request_div = document.getElementById('id_request');
    var result_div = document.getElementById('id_result');
    request_div.style.display = 'none';
    result_div.style.display = 'inline-flex';
}

function go_back() {
    var request_div = document.getElementById('id_request');
    var result_div = document.getElementById('id_result');
    request_div.style.display = 'inline-flex';
    result_div.style.display = 'none';
}