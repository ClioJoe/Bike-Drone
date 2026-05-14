const API_URL = "/api";

function toggleRentSize(isRenting) {
    const rentSizeGroup = document.getElementById('rentSizeGroup');
    const bikeSizeInput = document.getElementById('bikeSize');
    if (isRenting) {
        rentSizeGroup.classList.remove('hidden');
        bikeSizeInput.required = true;
    } else {
        rentSizeGroup.classList.add('hidden');
        bikeSizeInput.required = false;
    }
}

document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch(`${API_URL}/participants/`);
        const data = await response.json();

        const countElement = document.getElementById('count');
        if (countElement) countElement.innerText = data.total;

        const savedName = localStorage.getItem('aeroRideUser');
        if (savedName) {
            const found = data.participants.find(p =>
                `${p.firstName} ${p.lastName}`.toLowerCase() === savedName.toLowerCase()
            );
            if (found) {
                document.getElementById('alreadyRegistered').classList.remove('hidden');
                document.getElementById('registrationForm').classList.add('hidden');
            }
        }
    } catch (error) {
        console.error("Could not load participants:", error);
    }
});

document.getElementById('registrationForm')?.addEventListener('submit', async function(e) {
    e.preventDefault();

    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const isRenting = document.querySelector('input[name="bike"]:checked').value === 'rent';

    const newParticipant = {
        firstName: firstName,
        lastName: lastName,
        stravaScore: parseInt(document.getElementById('stravaScore').value),
        weight: parseFloat(document.getElementById('weight').value),
        level: document.getElementById('level').value,
        bikeStatus: isRenting ? `Renting (${document.getElementById('bikeSize').value})` : 'Own Bike',
        needs: document.getElementById('otherNeeds').value,
        droneConsent: document.getElementById('droneConsent').checked
    };

    try {
        const checkResponse = await fetch(`${API_URL}/participants/`);
        const checkData = await checkResponse.json();
        const alreadyExists = checkData.participants.find(p =>
            p.firstName.toLowerCase() === firstName.toLowerCase() &&
            p.lastName.toLowerCase() === lastName.toLowerCase()
        );

        if (alreadyExists) {
            localStorage.setItem('aeroRideUser', `${firstName} ${lastName}`);
            document.getElementById('alreadyRegistered').classList.remove('hidden');
            document.getElementById('registrationForm').classList.add('hidden');
            return;
        }

        const response = await fetch(`${API_URL}/participants/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newParticipant)
        });

        const data = await response.json();

        if (data.error) {
            alert("ACCESS DENIED: " + data.error);
            return;
        }

        localStorage.setItem('aeroRideUser', `${firstName} ${lastName}`);
        localStorage.setItem('lastRegistration', JSON.stringify(newParticipant));
        window.location.href = 'confirmation.html';

    } catch (error) {
        alert("Server error. Make sure the backend is running.");
        console.error(error);
    }
});