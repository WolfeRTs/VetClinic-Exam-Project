// Modal Elements
const modalContainer = document.getElementById('modalContainer');
const modalDescription = document.getElementById('modalDescription');
const modalDosages = document.getElementById('dosagesContent');
const modalTitle = document.getElementById('modalTitle');
const saveButton = document.getElementById('saveButton');
const deleteButton = document.getElementById('deleteButton');

// Initialize Tagify for services
var servicesInput = document.querySelector('#services-add-input');
var servicesTagify = new Tagify(servicesInput, {
    whitelist: [], // Optional if you have autocomplete
    enforceWhitelist: true,
    dropdown: {
        enabled: 0,
    }
});

// Fetch the services data and initialize Tagify
fetch('/services/api/services/')
    .then(response => response.json())
    .then(data => {
        servicesTagify.settings.whitelist = data.map(service => ({
            value: service.name,
            id: service.id,
            description: service.description,
        }));
    });

// Tagify Tag Click Handler
servicesTagify.on('click', function (e) {
    const tagData = e.detail.data;
    console.log('Tag clicked:', tagData);

    modalTitle.innerText = tagData.value;
    modalDescription.value = tagData.description || '';
    if (tagData.dosages) {
        modalDosages.value = tagData.dosages;
        document.getElementById('modalDosages').style.display = 'block';
    } else {
        document.getElementById('modalDosages').style.display = 'none';
    }

    saveButton.onclick = () => saveItem(tagData.id);
    deleteButton.onclick = () => deleteItem(tagData.id);

    modalContainer.style.display = 'flex';
});

// Modal Close on Outside Click
modalContainer.addEventListener('click', (e) => {
    if (e.target === modalContainer) {
        modalContainer.style.display = 'none';
    }
});

// Save Item Changes
function saveItem(itemId) {
    const updatedDescription = modalDescription.value;
    const updatedDosages = modalDosages.value;

    console.log('Saving item:', { id: itemId, updatedDescription, updatedDosages });

    fetch(`/services/api/services/${itemId}/`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            description: updatedDescription,
        }),
    })
    .then(response => response.json())
    .then(updatedItem => {
        console.log('Item saved:', updatedItem);

        // Update Tagify Whitelist
        servicesTagify.settings.whitelist = servicesTagify.settings.whitelist.map(item =>
            item.id === updatedItem.id
                ? { value: updatedItem.name, id: updatedItem.id, description: updatedItem.description }
                : item
        );
        modalContainer.style.display = 'none';
    })
    .catch(error => console.error('Error saving item:', error));
}

// Delete Item
function deleteItem(itemId) {
    if (confirm('Are you sure you want to delete this item?')) {
        console.log('Deleting item:', itemId);

        fetch(`/services/api/services/${itemId}/`, { method: 'DELETE' })
            .then(() => {
                console.log('Item deleted:', itemId);

                // Remove from Tagify
                servicesTagify.removeTag(itemId, true);
                modalContainer.style.display = 'none';
            })
            .catch(error => console.error('Error deleting item:', error));
    }
}

saveButton.addEventListener('click', saveItem);
deleteButton.addEventListener('click', deleteItem);