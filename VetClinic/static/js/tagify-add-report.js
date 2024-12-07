var servicesInput = document.querySelector('#services-add-input')
var medicinesInput = document.querySelector('#medicines-add-input')

servicesTagify = new Tagify(servicesInput, {
    whitelist: [],
    maxTags: 10,
    enforceWhitelist: true,
    editTags: false,
    dropdown: {
        maxItems: 10,
        classname: 'tags-look',
        enabled: 0,
        closeOnSelect: false
    }
})

medicinesTagify = new Tagify(medicinesInput, {
    whitelist: [],
    maxTags: 10,
    enforceWhitelist: true,
    editTags: false,
    dropdown: {
        maxItems: 20,
        classname: 'tags-look',
        enabled: 0,
        closeOnSelect: false
    }
})

fetch('/api/services/')
     .then(response => response.json())
     .then(data => {
         servicesTagify.settings.whitelist = data.map(service => ({
             value: service.name,
             id: service.id,
             description: service.description
         }));
     })
     .catch(error => console.error('Error fetching data:', error));

fetch('/api/medicines/')
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

var form = document.querySelector('#medical-report-form');
form.addEventListener('submit', (e) => {
    e.preventDefault();

    const selectedServiceTags = servicesTagify.value;
    const serviceIds = selectedServiceTags.map(tag => tag.id);
    const selectedMedicineTags = medicinesTagify.value;
    const medicineIds = selectedMedicineTags.map(tag => tag.id);

    servicesInput.value = JSON.stringify(serviceIds);
    medicinesInput.value = JSON.stringify(medicineIds);

    form.submit();
});
