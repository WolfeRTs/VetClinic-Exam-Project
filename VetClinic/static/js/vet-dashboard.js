const petsCategory = document.getElementById('pets');
const profilesCategory = document.getElementById('profiles');
const servicesCategory = document.getElementById('services');
const medicinesCategory = document.getElementById('medicines');

document.getElementById('search-bar').addEventListener('input', function (e) {
    const query = e.target.value.trim();
    const category = document.getElementById('search-category').value;

    if (query.length < 2) {
        clearSearchResults();
        return;
    }

    fetch(`/api/search/?q=${query}&category=${category}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            populateSearchResults(data, category);
        })
        .catch(error => console.error('Error fetching search results:', error));
});

function clearSearchResults() {
    ['pets', 'profiles', 'services', 'medicines'].forEach(category => {
        const ul = document.getElementById(category).querySelector('ul');
        ul.innerHTML = '';
    });
    petsCategory.style.display = 'none';
    profilesCategory.style.display = 'none';
    servicesCategory.style.display = 'none';
    medicinesCategory.style.display = 'none';
}

function populateSearchResults(data, category) {
    clearSearchResults();

    function displayCategoryResults(categoryData, categoryDiv, ul, urlPattern, categoryName) {
        categoryDiv.style.display = 'block';

        if (categoryData.length === 0) {
            const notFound = document.createElement('p');
            notFound.textContent = "No results found.";
            ul.appendChild(notFound);
            return;
        }

        categoryData.forEach(item => {
            const listItem = document.createElement('li');
            const link = document.createElement('a');
            link.href = urlPattern.replace('{id}', item.id);

            let displayText = '';
            if (categoryName === 'pets') {
                displayText = `${item.name} (Owner: ${item['owner__profile__first_name']})`;
            } else if (categoryName === 'profiles') {
                displayText = `${item['profile__first_name']} (${item['email']})`;
            } else if (categoryName === 'services') {
                displayText = `${item.name} - ${item.description}`;
            } else if (categoryName === 'medicines') {
                displayText = `${item.name} (Dosages: ${item.dosages})`;
            }

            link.textContent = displayText;
            listItem.appendChild(link);
            ul.appendChild(listItem);
        });
    }

    if (category === 'all' || category === 'pets') {
        const petsUl = petsCategory.querySelector('ul');
        displayCategoryResults(data.pets, petsCategory, petsUl, urlPatterns.pet, 'pets');
    }

    if (category === 'all' || category === 'profiles') {
        const profilesUl = profilesCategory.querySelector('ul');
        displayCategoryResults(data.profiles, profilesCategory, profilesUl, urlPatterns.profile, 'profiles');
    }

    if (category === 'all' || category === 'services') {
        const servicesUl = servicesCategory.querySelector('ul');
        displayCategoryResults(data.services, servicesCategory, servicesUl, urlPatterns.service, 'services');
        const buttonListElement = document.createElement('li');
        const buttonLink = document.createElement('a');
        buttonLink.href = urlPatterns.serviceAdd;
        buttonLink.textContent = 'Добави';
        buttonLink.classList.add('button-services');
        buttonListElement.appendChild(buttonLink);
        servicesUl.appendChild(buttonListElement);
    }

    if (category === 'all' || category === 'medicines') {
        const medicinesUl = medicinesCategory.querySelector('ul');
        displayCategoryResults(data.medicines, medicinesCategory, medicinesUl, urlPatterns.medicine, 'medicines');
        const buttonListElement = document.createElement('li');
        const buttonLink = document.createElement('a');
        buttonLink.href = urlPatterns.medicineAdd;
        buttonLink.classList.add('button-services');
        buttonLink.textContent = 'Добави';
        buttonListElement.appendChild(buttonLink);
        medicinesUl.appendChild(buttonListElement);
    }
}


// function populateSearchResults(data, category) {
//     clearSearchResults();
//
//     // Filter based on selected category
//     if (category === 'all' || category === 'pets') {
//         const petsUl = document.getElementById('pets').querySelector('ul');
//         petsCategory.style.display = 'block';
//         if (data.pets.length === 0) {
//             const notFound = document.createElement('p');
//             notFound.textContent = "No results found.";
//             petsUl.appendChild(notFound);
//         }
//         data.pets.forEach(pet => {
//             const item = document.createElement('li');
//             const link = document.createElement('a')
//             link.href = urlPatterns.pet.replace('{id}', pet.id);
//             item.textContent = `${pet.name} (Owner: ${pet['owner__profile__first_name']})`;
//             link.appendChild(item);
//             petsUl.appendChild(link);
//         });
//     }
//
//     if (category === 'all' || category === 'profiles') {
//         const profilesUl = document.getElementById('profiles').querySelector('ul');
//         profilesCategory.style.display = 'block';
//         if (data.profiles.length === 0) {
//             const notFound = document.createElement('p');
//             notFound.textContent = "No results found.";
//             profilesUl.appendChild(notFound);
//         }
//         data.profiles.forEach(profile => {
//             const item = document.createElement('li');
//             const link = document.createElement('a')
//             link.href = urlPatterns.profile.replace('{id}', profile['user__id']);
//             item.textContent = `${profile['first_name']} (${profile['user__email']})`;
//             link.appendChild(item);
//             profilesUl.appendChild(link);
//         });
//     }
//
//     if (category === 'all' || category === 'services') {
//         const servicesUl = document.getElementById('services').querySelector('ul');
//         servicesCategory.style.display = 'block';
//         if (data.services.length === 0) {
//             const notFound = document.createElement('p');
//             notFound.textContent = "No results found.";
//             servicesUl.appendChild(notFound);
//         }
//         data.services.forEach(service => {
//             const item = document.createElement('li');
//             const link = document.createElement('a')
//             link.href = urlPatterns.service.replace('{id}', service.id);
//             item.textContent = `${service.name} - ${service.description}`;
//             link.appendChild(item);
//             servicesUl.appendChild(link);
//         });
//     }
//
//     if (category === 'all' || category === 'medicines') {
//         const medicinesUl = document.getElementById('medicines').querySelector('ul');
//         medicinesCategory.style.display = 'block';
//         if (data.medicines.length === 0) {
//             const notFound = document.createElement('p');
//             notFound.textContent = "No results found.";
//             medicinesUl.appendChild(notFound);
//         }
//         data.medicines.forEach(medicine => {
//             const item = document.createElement('li');
//             const link = document.createElement('a')
//             link.href = urlPatterns.medicine.replace('{id}', medicine.id);
//             item.textContent = `${medicine.name} (Dosages: ${medicine.dosages})`;
//             link.appendChild(item);
//             medicinesUl.appendChild(link);
//         });
//     }
// }
