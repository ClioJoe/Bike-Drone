// Toggle bike rent size
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

// Load participant count on page load
document.addEventListener('DOMContentLoaded', () => {
    const participants = JSON.parse(localStorage.getItem('aeroRideParticipants')) || [];
    const countElement = document.getElementById('count');
    if (countElement) {
        countElement.innerText = participants.length;
    }
});

// Form submission
document.getElementById('registrationForm')?.addEventListener('submit', function(e) {
    e.preventDefault();

    let participants = JSON.parse(localStorage.getItem('aeroRideParticipants')) || [];

    if (participants.length >= 50) {
        alert("ACCESS DENIED: Registration is full. Maximum 50 participants reached.");
        return;
    }

    const isRenting = document.querySelector('input[name="bike"]:checked').value === 'rent';

    const newParticipant = {
        firstName: document.getElementById('firstName').value,
        lastName: document.getElementById('lastName').value,
        stravaScore: parseInt(document.getElementById('stravaScore').value),
        weight: document.getElementById('weight').value,
        level: document.getElementById('level').value,
        bikeStatus: isRenting ? `Renting (${document.getElementById('bikeSize').value})` : 'Own Bike',
        needs: document.getElementById('otherNeeds').value,
        droneConsent: document.getElementById('droneConsent').checked
    };

    participants.push(newParticipant);
    localStorage.setItem('aeroRideParticipants', JSON.stringify(participants));

    window.location.href = 'leaderboard.html';
});