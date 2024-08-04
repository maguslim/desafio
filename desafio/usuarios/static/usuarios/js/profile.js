function toggleEditMode() {
    const editCheckbox = document.getElementById('edit-checkbox');
    const formControls = document.querySelectorAll('.form-control');
    const saveButton = document.querySelector('.save-button');
    const editButton = document.querySelector('.edit-button');
    const profilePictureButton = document.querySelector('.profile-picture-button');
    const removePictureButton = document.querySelector('.btn-danger');
    
    if (editCheckbox.checked) {
        editCheckbox.checked = false;
        formControls.forEach(control => control.setAttribute('readonly', true));
        profilePictureButton.setAttribute('disabled', true);
        saveButton.style.display = 'none';
        editButton.style.display = 'block';
        if (removePictureButton) removePictureButton.setAttribute('disabled', true);
    } else {
        editCheckbox.checked = true;
        formControls.forEach(control => control.removeAttribute('readonly'));
        profilePictureButton.removeAttribute('disabled');
        saveButton.style.display = 'block';
        editButton.style.display = 'none';
        if (removePictureButton) removePictureButton.removeAttribute('disabled');
    }
}

// Atualiza a imagem de perfil em tempo real
document.getElementById('id_profile_picture').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('profile-picture').src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
});

document.getElementById('id_phone_number').addEventListener('input', function(event) {
    let value = event.target.value.replace(/\D/g, ''); // Remove todos os caracteres não numéricos

    if (value.length > 11) {
        value = value.slice(0, 11); // Limita o número de caracteres a 11
    }

    let formattedValue = '';

    // Aplica a formatação conforme o número de caracteres
    if (value.length > 6) {
        formattedValue = `(${value.slice(0, 2)})${value.slice(2, 7)}-${value.slice(7)}`;
    } else if (value.length > 2) {
        formattedValue = `(${value.slice(0, 2)})${value.slice(2)}`;
    } else {
        formattedValue = value;
    }

    // Atualiza o valor do input com a formatação aplicada
    event.target.value = formattedValue;
});