// main.js

document.addEventListener("DOMContentLoaded", function () {
    const initialState = loadCheckboxState();
    updateTrackerSpan(initialState);

    const checkboxes = document.querySelectorAll('.checkbox');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', handleCheckboxChange);
    });

    const editPreferencesSpan = document.querySelector('.v6_679');
    editPreferencesSpan.addEventListener('click', handleEditPreferencesClick);
});

function handleCheckboxChange(event) {
    const checkbox = event.target;
    const currentState = loadCheckboxState();
    currentState[checkbox.classList[1]] = checkbox.checked;
    saveCheckboxState(currentState);
    updateTrackerSpan(currentState);
}

function handleEditPreferencesClick() {
    const hideVideosCheckbox = document.getElementById('hideVideos');
    
    if (hideVideosCheckbox) {
        hideVideosCheckbox.checked = !hideVideosCheckbox.checked;

        // Update the JSON object with the new checkbox state
        const currentState = loadCheckboxState();
        currentState['hideVideos'] = hideVideosCheckbox.checked;

        // Save the updated JSON object to the JSON file
        saveCheckboxState(currentState);

        // Update the tracker span based on the checkbox states
        updateTrackerSpan(currentState);
    }
}

function loadCheckboxState() {
    const jsonData = '{"v6_25": false, "v6_26": false, "v6_27": false, "v6_28": false}';
    return JSON.parse(jsonData);
}

function saveCheckboxState(state) {
    const jsonString = JSON.stringify(state);
    console.log('Saving state to JSON file:', jsonString);
}

function updateTrackerSpan(state) {
    const trackerSpan = document.querySelector('.v6_679');
    trackerSpan.textContent = 'Confirm';
}
