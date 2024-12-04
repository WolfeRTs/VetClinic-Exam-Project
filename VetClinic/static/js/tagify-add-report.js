var servicesInput = document.querySelector('#services-add-input')
var medicinesInput = document.querySelector('#medicines-add-input')

servicesTagify = new Tagify(servicesInput, {
    whitelist: [],
    maxTags: 10,
    enforceWhitelist: true,
    editTags: false,
    dropdown: {
        maxItems: 20,           // <- maximum allowed rendered suggestions
        classname: 'tags-look', // <- custom classname for this dropdown, so it could be targeted
        enabled: 0,             // <- show suggestions on focus
        closeOnSelect: false    // <- do not hide the suggestions dropdown once an item has been selected
    }
})

medicinesTagify = new Tagify(medicinesInput, {
    whitelist: [],
    maxTags: 10,
    enforceWhitelist: true,
    editTags: false,
    dropdown: {
        maxItems: 20,           // <- maximum allowed rendered suggestions
        classname: 'tags-look', // <- custom classname for this dropdown, so it could be targeted
        enabled: 0,             // <- show suggestions on focus
        closeOnSelect: false    // <- do not hide the suggestions dropdown once an item has been selected
    }
})

fetch('/services/api/services/')
     .then(response => response.json())
     .then(data => {
         servicesTagify.settings.whitelist = data.map(service => ({
             value: service.name,
             id: service.id,
             description: service.description
         }));
     })
     .catch(error => console.error('Error fetching data:', error));

fetch('/services/api/medicines/')
     .then(response => response.json())
     .then(data => {
         medicinesTagify.settings.whitelist = data.map(medicine => ({
             value: medicine.name,
             id: medicine.id,
             description: medicine.description,
             dosages: medicine.dosages
         }));
     })
     .catch(error => console.error('Error fetching data:', error));

// Handle form submission
var form = document.querySelector('#medical-report-form');
form.addEventListener('submit', (e) => {
    e.preventDefault();
    // Extract selected service IDs
    const selectedServiceTags = servicesTagify.value;
    const serviceIds = selectedServiceTags.map(tag => tag.id);
    const selectedMedicineTags = medicinesTagify.value;
    const medicineIds = selectedMedicineTags.map(tag => tag.id);

    servicesInput.value = JSON.stringify(serviceIds);
    medicinesInput.value = JSON.stringify(medicineIds);

    // // Add service IDs to the form as a hidden input
    // const hiddenInput = document.createElement('input');
    // hiddenInput.type = 'hidden';
    // hiddenInput.name = 'services';
    // hiddenInput.value = JSON.stringify(serviceIds);
    // form.appendChild(hiddenInput);

    // Submit the form
    form.submit();
});
