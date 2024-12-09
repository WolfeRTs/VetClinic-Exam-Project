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
            notFound.textContent = gettext("No results found.");
            ul.appendChild(notFound);
            return;
        }

        categoryData.forEach(item => {
            const listItem = document.createElement('li');
            const link = document.createElement('a');
            link.href = urlPattern.replace('{id}', item.id);

            let displayText = '';
            if (categoryName === 'pets') {
                const firstName = item['owner__profile__first_name'] || '';
                const lastName = item['owner__profile__last_name'] || '';
                displayText = `${item.name} (${item['owner__username']})`;

                if (firstName || lastName) {
                    displayText += ` - ${firstName} ${lastName}`;
                }
            } else if (categoryName === 'profiles') {
                const firstName = item['profile__first_name'] || '';
                const lastName = item['profile__last_name'] || '';
                displayText = `${item['username']} (${item['email']})`;

                if (firstName || lastName) {
                    displayText += ` - ${firstName} ${lastName}`;
                }
            } else if (categoryName === 'services') {
                displayText = `${item.name} - ${item.description}`;
            } else if (categoryName === 'medicines') {
                displayText = `${item.name} (${item.dosages})`;
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
        buttonLink.textContent = gettext('Добави');
        buttonListElement.classList.add('button-services-li');
        buttonListElement.appendChild(buttonLink);
        servicesUl.appendChild(buttonListElement);
    }

    if (category === 'all' || category === 'medicines') {
        const medicinesUl = medicinesCategory.querySelector('ul');
        displayCategoryResults(data.medicines, medicinesCategory, medicinesUl, urlPatterns.medicine, 'medicines');
        const buttonListElement = document.createElement('li');
        const buttonLink = document.createElement('a');
        buttonLink.href = urlPatterns.medicineAdd;
        buttonLink.textContent = gettext('Добави');
        buttonListElement.classList.add('button-services-li');
        buttonListElement.appendChild(buttonLink);
        medicinesUl.appendChild(buttonListElement);
    }
}
