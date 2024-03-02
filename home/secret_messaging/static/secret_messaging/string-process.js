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